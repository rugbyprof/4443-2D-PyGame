import sys
import os
import json
import pprint as pp

# PyIntro Lesson 20
# Classes Part 1

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

# {
#     "fname":"Sasha",
#     "lname":"Ivanov",
#     "rank": 15339,
#     "screen_name":"spetsnaz983",
#     "email":"sashaivanov1998@gru.gov",
#     "power-boost":98.34,
#     "available-boosts": ["skull-crush","flower-child","acid-trip","disco-ball"]
# }

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        players = getattr(self, "players", None)
        if not players:
            self.players = []

class LeaderBoard(Borg):
        def __init__(self, player=None):
            Borg.__init__(self)
            if player is not None:
                self.players.append(player)
        def __str__(self):
            str = ""
            i = 0
            for p in self.players:
                str += f"{i} : {p}\n"
                i += 1
            return str

class Player:
    def __init__(self,**kwargs):
        self.fname = kwargs.get("fname",None)
        self.lname = kwargs.get("lname",None)
        self.rank = kwargs.get("rank",None)
        self.email = kwargs.get("email",None)
        self.screenName = kwargs.get("screen_name",None)
        self.powerBoost = kwargs.get("power-boost",None)
        self.availableBoosts = kwargs.get("available-boosts",[])
        self.leaderBoard = LeaderBoard(self.screenName)

    def __str__(self):
        str =  f"First: {self.fname} Last: {self.lname}"
        str += f"\nRank: {self.rank} Email: {self.email}"
        str += f"PowerBoost: {self.powerBoost}\n"
        str += "AvailableBoosts: "
        for boost in self.availableBoosts:
            str += boost + " "
        return str + "\n"


    def updatePlayer(self,**kwargs):
        for key,val in kwargs.items():
            if val:
                setattr(self, key, val)


if __name__=='__main__':

    lb = LeaderBoard()

    jdata = readJson("./data/player1Data.json")

    p1 = Player(**jdata)

    jdata = readJson("./data/player2Data.json")

    p2 = Player(**jdata)

    print(p1)
    print(p2)

    p2.updatePlayer(rank=55)

    print(p2)

    print(lb)


