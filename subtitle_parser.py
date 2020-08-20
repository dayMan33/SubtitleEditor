import codecs
from typing import List
from datetime import timedelta
from subtitle import Subtitle
from subtitle_sequence import SubtitleSequence


class SubtitleParser(object):
    SUBTITLE_DELIMITERS = {'\r\n', '\n', '\t\n'}
    TIME = 1
    TEXT_BEGINING = 2

    forbidden_texts = {'<font color="#ffff00" size=14>www.tvsubtitles.net</font>'}

    @staticmethod
    def parse_subtitle_file(filepath: str) -> SubtitleSequence:
        if not SubtitleParser._is_srt_file(filepath):
            raise IOError('Unsupported file format. Can only operate of SubRip files (files that end with \".srt\"')
        with open(filepath) as file:
            lines = file.readlines()
            sequence = SubtitleSequence()
            while lines:
                subtitle = SubtitleParser._extract_subtitle(lines)
                if subtitle:
                    sequence.add_subtitle(subtitle)
        return sequence

    @staticmethod
    def _extract_subtitle(lines: List[str]) -> Subtitle:
        subtitle_data = []
        while lines and lines[0] not in SubtitleParser.SUBTITLE_DELIMITERS:
            subtitle_data.append(lines.pop(0))
        while lines and lines[0] in SubtitleParser.SUBTITLE_DELIMITERS:
            lines.pop(0)  # Remove the empty lines between subtitles.
        appear, dissapear = SubtitleParser._parse_subtitle_time(subtitle_data[SubtitleParser.TIME])
        text = SubtitleParser._parse_subtitle_text(subtitle_data[SubtitleParser.TEXT_BEGINING:])
        if not text:
            return
        return Subtitle(appear, dissapear, text)

    @staticmethod
    def _parse_subtitle_time(time_line):
        appear_text, dissapear_text = time_line.split('-->')
        return SubtitleParser._str_to_time(appear_text), SubtitleParser._str_to_time(dissapear_text)

    @staticmethod
    def _is_srt_file(filepath):
        return filepath.endswith('.srt')

    @staticmethod
    def _str_to_time(time_str) -> timedelta:
        hours, min, sec = time_str.split(':')
        sec, millisec = sec.split(',')
        return timedelta(hours=int(hours), minutes=int(min), seconds=int(sec), milliseconds=int(millisec))

    @classmethod
    def _parse_subtitle_text(cls, text_lines):
        text = []
        for line in text_lines:
            line = line.strip()
            if line in SubtitleParser.forbidden_texts:
                continue
            text.append(line)
        return text

