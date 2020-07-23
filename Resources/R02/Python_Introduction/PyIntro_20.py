import math
import os,sys
import json

# PyIntro Lesson 20
# Classes Part 1


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




