import sys
import os
import pprint as pp
import json

# PyIntro Lesson 15
# Reading Files
# reading json file into a dictionary
# writing json to a file

fpath = "playerData.json"
outpath = "newPlayerData.json"

if os.path.isfile(fpath):
    f = open(fpath,"r")
    data = f.read()
    f.close()
else:
    print("Error: File doesn't exist!")

print(data)
print(type(data))

player = json.loads(data)

pp.pprint(player)
print(type(player))

player["rank"] = 20202020
player["available-boosts"].append("bourbon-liver")

f = open(outpath,"w")

f.write(json.dumps(player))


