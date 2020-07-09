import sys
import os
import pprint as pp

# PyIntro Lesson 12
# Dictionaries

lst = [{},{},{}]

d = {
    "apples":100,
    "bananas":200,
    "cherries":150,
    "donuts":1000,
    "eclaires":40,
    "falafel":30,
    "grapes":2,
    "halibut":99,
    "ice cream":345,
    100:1000
}

print(d.get("hooble","out of stock"))

x = d.setdefault("grapes",0)

print(x)

pp.pprint(d)












