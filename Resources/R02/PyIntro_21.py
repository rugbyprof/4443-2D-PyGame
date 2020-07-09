import math
import os,sys
import json

# PyIntro Lesson 21
# Classes Part 2

class Data:
    @staticmethod
    def validJson(jdata):
        try:
            json_object = json.loads(jdata)
            return True
        except ValueError as e:
            pass
        return False

    @staticmethod
    def readJson(loc_path):
        if os.path.isfile(loc_path):
            f = open(loc_path,"r")
            data = f.read()
            if Data.validJson(data):
                jdata = json.loads(data)
                if jdata:
                    return jdata
                else:
                    return None
        return None



class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x:{self.y},y:{self.y})"

    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)

    def __sub__(self,other):
        return Point(self.x - other.x , self.y - other.y)

    def distance(self,other):
        return math.sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))


if __name__=='__main__':
    data_folder = "./data/"
    file_name = 'player2Data.json'

    path = os.path.join(data_folder,file_name)

    print(path)

    print(Data.readJson(path))




