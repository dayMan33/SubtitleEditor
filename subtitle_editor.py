import sys
from subtitle_sequence import SubtitleSequence
from subtitle_writer import SubtitleWriter
from subtitle_parser import SubtitleParser
from datetime import timedelta
import argparse


def create_argparser():
    parser = argparse.ArgumentParser(description='Shift the timing in a subtitle SubRip file.')
    parser.add_argument('file', help='An input file of type SubRip to edit')
    parser.add_argument('-out_file', nargs='?',
                        help='A file to write into. If not specified, would write into the input file specified')
    parser.add_argument('-neg', action='store_true', default=False, help='Indicates whether the subtitles should be'
                                                                         'shifted forward or backwards. Specifying '
                                                                         '\'-neg\' means the subtitles\' appearing time'
                                                                         'should be shifted so that they appear earlier')
    parser.add_argument('-hour', nargs='?', default=0, type=int,
                        help='By how many hours should the subtitles be shifted ')
    parser.add_argument('-min', nargs='?', default=0, type=int,
                        help='By how many minutes should the subtitles be shifted ')
    parser.add_argument('-sec', nargs='?', default=0, type=int,
                        help='By how many seconds should the subtitles be shifted ')
    parser.add_argument('-mil', nargs='?', default=0, type=int,
                        help='By how many milliseconds should the subtitles be shifted ')
    return parser


if __name__ == '__main__':
    arg_parser = create_argparser()
    args = arg_parser.parse_args()

    sequence = SubtitleParser.parse_subtitle_file(args.file)
    time = timedelta(hours=args.hour, minutes=args.min, seconds=args.sec, milliseconds=args.mil)
    sequence.adjust_time_for_all(time, args.neg)
    if args.out_file == None:
        args.out_file = args.file
    SubtitleWriter.write_subtitle_sequence(sequence, args.out_file)
