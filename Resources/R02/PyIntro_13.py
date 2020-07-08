import sys
import os
import pprint as pp

# PyIntro Lesson 13
# Dictionaries part deux

d = {
    "apples":100,
    "bananas":200,
    "cherries":150,
    "donuts":1000,
    "eclaires":40,
    "falafel":30,
    "grapes":2,
    "halibut":99,
    "ice cream":345
}

for key in d:
    print(key,":",d[key])

k,v = ("apples",100)

for k,v in d.items():
    print(k,v)

print("="*80)

class_grades = {
    "smith":[88,66,77],
    "goldburg":[99,88,77],
    "kalawani":[99,66,99],
    "gandolph":[100,0,50]
}

for name,grades in class_grades.items():
    sum = 0
    for g in grades:
        #print(g)
        sum += g
    print(name,":",round(g/len(grades),2))

print("="*80)

randy = {
    "key":1000,
    "list":[6,7,8,9],
    "dict":{"subkey1":"subval1","subkey2":"subval2","subkey3":"subval3"}
}

for k,v in randy.items():
    if type(v) is list:
        for sv in v:
            print(sv)
    elif type(v) is dict:
        for sk,sv in v.items():
            print(sk,":",sv)
    else:
        print(k,v)






