from datetime import timedelta
from typing import List


class IllegalTimeError(RuntimeError):
    pass


class Subtitle:

    def __init__(self, appear_time: timedelta, off_time: timedelta, text: List[str]):
        self._appear_time = appear_time
        self._disappear_time = off_time
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def appear_time(self):
        return self._appear_time

    @appear_time.setter
    def appear_time(self, time=timedelta):
        if self.disappear_time <= time:
            raise IllegalTimeError('subtitle appear_time cannot follow disappear_time')
        self.appear_time = time

    @property
    def disappear_time(self):
        return self._disappear_time

    @disappear_time.setter
    def disappear_time(self, time: timedelta):
        if self.appear_time >= time:
            raise IllegalTimeError('subtitle disappear_time cannot precede appear_time')
        self.disappear_time = time

    def adjust_time(self, delay=timedelta, neg: bool = False):
        if neg:
            if delay > self.appear_time:
                raise IllegalTimeError('Subtitle appear time cannot be negative. ')
            self._appear_time -= delay
            self._disappear_time -= delay
        else:
            self._appear_time += delay
            self._disappear_time += delay
