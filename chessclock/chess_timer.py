# coding: utf-8
import datetime
import time

class player():
    """
    way1. loop pmain and use interrupt
    way2. use set_dt1 and calc
    """

    def __init__(self):
        now = datetime.datetime.now()
        self.t = datetime.datetime(now.year,now.month,now.day,hour=0,minute=1,second=0,microsecond=0)
        self.zero = datetime.datetime(now.year,now.month,now.day,hour=0,minute=0,second=0,microsecond=0)
        self.pflag = False

    def pmain(self):
        dt1 = datetime.datetime.now()
        while 1:
            if self.pflag:
                dt2 = datetime.datetime.now()
                d = abs(dt2 - dt1)
                if d.microseconds > 500000 or d.seconds > 0:
                    print(self.t)
                    dt1 = datetime.datetime.now()
                    self.t -= d
                if self.t < self.zero:
                    print('Game Over.')
                    break

    def set_dt1(self):
        self.dt1 = datetime.datetime.now()

    def calc(self):
        dt2 = datetime.datetime.now()
        d = abs(dt2 - self.dt1)
        if d.microseconds > 500000 or d.seconds > 0:
            dt1 = datetime.datetime.now()
            self.t -= d
        if self.t < self.zero:
            print('Game Over.')

if __name__ == '__main__':
    p1 = player()
    p1.pflag = True
