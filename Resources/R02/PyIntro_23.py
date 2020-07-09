import math
import os,sys
import json

# PyIntro Lesson 23
# Classes Part 4

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

class Player:
    def __init__(self,**kwargs):
        self.fname = kwargs.get("fname",None)
        self.lname = kwargs.get("lname",None)
        self.rank = kwargs.get("rank",None)
        self.email = kwargs.get("email",None)
        self.screenName = kwargs.get("screen_name",None)
        self.powerBoost = kwargs.get("power-boost",None)
        self.availableBoosts = kwargs.get("available-boosts",[])

    def __str__(self):
        str =  f"First: {self.fname} Last: {self.lname}"
        str += f"\nRank: {self.rank} Email: {self.email}"
        str += f"PowerBoost: {self.powerBoost}\n"
        str += "AvailableBoosts: "
        for boost in self.availableBoosts:
            str += boost + " "
        return str + "\n"

    def addBoost(self,boosts=[]):
        """
        Parameters
        ----------
        boost : list
           List of player boosts to add to a players character

        Returns
        -------
            None
        """
        self.availableBoosts.extend(boosts)

    def updatePlayer(self,**kwargs):
        """
        Parameters
        ----------
        fname : str, optional
            player first name
        lname : str, optional
            player last name
        rank : int, optional
            player rank on leader boards
        ... (+ more)
        """
        for key,val in kwargs.items():
            if val:
                setattr(self, key, val)




if __name__=='__main__':
    data_folder = "./data/"
    file_name = 'player1Data.json'

    player1Dict= Data.readJson(os.path.join(data_folder,file_name))

    p1 = Player(**player1Dict)

    p2 = Player(fname="bob",lname="smith")

    print(p2)

    help(p1)
