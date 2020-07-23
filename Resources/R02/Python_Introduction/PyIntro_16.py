import sys
import os
import json
import pprint as pp

# PyIntro Lesson 16
# Functions

file_path = "./FileRead/playerData.json"

def validJson(jdata):
    try:
        json_object = json.loads(jdata)
        return True
    except ValueError as e:
        pass
    return False

def readJson(loc_path):
    if os.path.isfile(loc_path):
        f = open(loc_path,"r")
        data = f.read()
        if validJson(data):
            jdata = json.loads(data)
            if jdata:
                return jdata
            else:
                return None
    return None



myjsondata = readJson(file_path)

if myjsondata:
    pp.pprint(myjsondata)
else:
    print("Ooops!!")




