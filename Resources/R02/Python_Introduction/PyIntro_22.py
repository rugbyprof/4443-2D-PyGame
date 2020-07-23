import math
import os,sys
import json

# PyIntro Lesson 22
# Classes Part 3

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
        return f"(x:{self.x},y:{self.y})"

    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)

    def __sub__(self,other):
        return Point(self.x - other.x , self.y - other.y)

    def distance(self,other):
        return math.sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))

    def get(self):
        return self.x, self.y

    def set(self,x,y=None):
        if not y:
            if type(x) == list or type(x) == tuple:
                self.x = x[0]
                self.y = x[1]
        else:
            self.x = x
            self.y = y






if __name__=='__main__':
    data_folder = "./data/"
    file_name = 'player2Data.json'

    p1 = Point(6,8)

    print(p1)

    x,y = p1.get()

    print(x,y)

    p1.set(12,12)

    print(p1)

    p1.set([78,45])

    print(p1)

    p1.set((99,99))

    print(p1)




