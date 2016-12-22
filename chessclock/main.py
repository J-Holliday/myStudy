from chess_timer import player
import time

"""
It is not used interrupt
"""

p1 = player()
p2 = player()

while 1:
    p1.set_dt1()
    time.sleep(3)
    if 1:
        p1.calc()
        print(p1.t, p2.t)
        p2.set_dt1()
        time.sleep(3)
        print(2)
        p2.calc()
        print(p1.t, p2.t)
