import sys
import os

# PyIntro Lesson 11
# Tuples
# mutable
# tuples are immutable

t = ('hello','world')

print(t)

print(type(t))


t1 = (1,2,3,4,5)
t2 = (4,5,6,7)

t3 = t1+t2

print(t3)

print(max(t3))
print(min(t3))

t3 = list(t3)

print(t3)

t4 = (44,77,100)

x,y,z = t4

print(f"x:{x} , y:{y} z:{z}")
