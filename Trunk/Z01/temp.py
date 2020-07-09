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


def SimpleAdd(a,b):
    return a + b

def BetterAdd(a,b=0,c=0):
    return a + b + c

def BetterAdd(a,b,c):
    return a + b + c

def SuperAdd(*args):
    sum = 0
    for a in args:
        sum += a
    return sum

def CrazyAdd(func,param,*args):
    ans = 0
    for a in args:
        if param:
            ans = func(a,param)
        else:
            ans = func(a)

    return ans

if __name__=='__main__':
    # x = SimpleAdd(4,5)
    # print(x)
    # x = BetterAdd(4)
    # print(x)

    x = CrazyAdd(math.pow,2,6,2,3,4,5,6,7,8)
    print(x)

def playerUpdater(player,**kwargs):
    fname = kwargs.get("fname",None)
    lname = kwargs.get("lname",None)
    rank = kwargs.get("rank",None)
    email = kwargs.get("email",None)
    powerBoost = kwargs.get("power-boost",None)
    print(player)
    print(kwargs)


    class Vector:
        def __init__(self,x=0,y=0):
            self.a = 0
            self.b = 0

        def __str__(self):
            return f"(a:{self.a},b:{self.b})"

        def __add__(self,other):
            return Vector(self.a + other.a , self.b + other.b)

        def __sub__(self,other):
            return Vector(self.a - other.a , self.b - other.b)
