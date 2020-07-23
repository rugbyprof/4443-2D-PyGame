import sys
import os
import json
import math



# PyIntro Lesson 18
# Functions Part 2
# default arguments
# args

def SimpleAdd(a,b=0):
    return a + b

def BetterAdd(a,b,c):
    return a + b + c

def SuperMethod(func,param,*args):
    ans = 0

    for a in args:
        ans = func(a,param)

    return ans

if __name__=='__main__':
    x = SimpleAdd(2)
    print(x)

    x = SuperMethod(math.pow,2,3,4,5,2,3,4,5,6)
    print(x)








