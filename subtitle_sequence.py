import datetime


class SubtitleSequence:

    def __init__(self):
        self.sequence = []

    def adjust_time_for_all(self, time: datetime, neg: bool = False):
        for i in range(len(self.sequence)):
            self.adjust_time(time, i, neg)

    def adjust_time(self, time, index, neg):
        if index < len(self.sequence):
            self.sequence[index].adjust_time(time, neg)

    def add_subtitle(self, subtitle, index=None):
        if index is None:
            self.sequence.append(subtitle)
        else:
            self.sequence.insert(index - 1, subtitle)

    def pop(self, index=0):
        return self.sequence.pop(index)

    def __getitem__(self, index):
        return self.sequence[index]

    def __bool__(self):
        return bool(self.sequence)
