import sys
import os
import pprint

# PyIntro Lesson 12
# Dictionaries

lst = [5,6,7,"hello",99.9]

d = {
    "apples":100,
    "bananas":200,
    "cherries":150,
    "donuts":1000,
    "eclaires":40,
    "falafel":30,
    "goo":2
}

pprint.pprint(d)

# print(d["apples"])

for i in d:
    print(d[i])


for key,val in d.items():
    print(f"key: {key} , val: {val}")

print(d.keys())
print(d.values())

d["newitem"] = 888

pprint.pprint(d)


