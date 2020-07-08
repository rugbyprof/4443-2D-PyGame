import sys
import os

# PyIntro Lesson 08
# for loop
# while loop
# break
# continue

for c in "hello world":
    print(c)

val = 1

while(val) :
    val = input("Enter a number: ")
    if val:
        break
    print(f"You entered {val} ...")