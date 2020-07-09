import sys
import os
import json
import pprint as pp

# PyIntro Lesson 19
# Functions Part 3
# kwargs



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

def playerUpdater(player,**kwargs):
    fname = kwargs.get("fname",None)
    lname = kwargs.get("lname",None)
    rank = kwargs.get("rank",None)
    email = kwargs.get("email",None)
    powerBoost = kwargs.get("power-boost",None)

    if fname:
        player['fname'] = fname
    if lname:
        player['lname'] = lname
    if email:
        player['email'] = email
    if rank:
        player['rank'] = rank

    return player

if __name__=='__main__':
    jdata = readJson("./data/playerData.json")

    pp.pprint(jdata)

    updated = playerUpdater(jdata,fname="Bob",email="bobthebiulder@gamil.com",rank=999999)

    pp.pprint(updated)










