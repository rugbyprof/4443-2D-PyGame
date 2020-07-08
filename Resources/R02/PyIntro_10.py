import sys
import os

# PyIntro Lesson 10
# Lists (part 2)
# mutating and slicing
# range function

lst = [10,20,30,40,50]
print(lst)

print(lst[0])
print(lst[-1])
print(lst[-2])

#lst[ start slice : end slice]
print(lst[1:3])
print(lst[:3])
print(lst[3:])
print(lst[:-1])

# lst [ start : end : step]
print(lst[::2])
print(lst[::-1])
print(lst[::-2])

del lst[3]
print(lst)

lst[3] = 40
print(lst)

lst[3] = [40,50]
print(lst)

for i in range(10):
    print(i)
print("")
for i in range(10,20):
    print(i)
print("")
for i in range(0,20,2):
    print(i)