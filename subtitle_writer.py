from subtitle_sequence import SubtitleSequence
from subtitle import Subtitle
from datetime import timedelta


class SubtitleWriter(object):

    @staticmethod
    def write_subtitle_sequence(sequence: SubtitleSequence, file_path: str):
        with open(file_path, 'w') as file:
            i = 1
            while sequence:
                file.writelines(SubtitleWriter._subtitle_to_lines(sequence.pop(), i))
                i += 1

    @staticmethod
    def _subtitle_to_lines(subtitle: Subtitle, id: int):
        lines = [str(id)]
        lines.append(SubtitleWriter._subtitle_time_to_str(subtitle))
        lines = lines + subtitle.text
        lines.append('\n')

        return '\n'.join(lines)

    @staticmethod
    def _subtitle_time_to_str(subtitle):
        appear_time = SubtitleWriter._time_to_str(subtitle.appear_time)
        disappear_time = SubtitleWriter._time_to_str(subtitle.disappear_time)
        return appear_time + ' --> ' + disappear_time

    @staticmethod
    def _time_to_str(time: timedelta):
        hours = SubtitleWriter._adjust_time_str(str(time.days * 24 + time.seconds // 3600))
        minutes = SubtitleWriter._adjust_time_str(str((time.seconds % 3600) // 60))
        seconds = SubtitleWriter._adjust_time_str(str(time.seconds % 60))
        millisec = str(time.microseconds * 1000)[:3]
        return ','.join([':'.join([hours, minutes, seconds]), millisec])

    @staticmethod
    def _adjust_time_str(time_str):
        if len(time_str) < 2:
            time_str = ('0' * (2 - len(time_str))) + time_str
        return time_str
