# temp
# https://realpython.com/python3-object-oriented-programming/

class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0


def Add(fname,lname,*args):
    sum = 0
    for arg in args:
        sum += int(arg)
    return sum

one = 99
two = 77
three = 88
four = 77
five = 36
six = 400

sum = Add(one,two,three,four,five,six)

print(sum)

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do#:~:text=Consider%3A%20if%20__name__,case%20the%20main()%20function).

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

import FakeMathModule
from FakeMathModule import add
from FakeMathModule import *
