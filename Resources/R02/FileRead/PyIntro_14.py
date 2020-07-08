import sys
import os
import pprint as pp

# PyIntro Lesson 14
# Reading Files
# read       - all at once
# readlines  - into a list 1 line per entry
# readline   - reads one line

fpath = "chuck.dat"

if os.path.isfile(fpath):
    f = open(fpath,"r")
    data = f.read()
    f.close()
else:
    print("Error: File doesn't exist!")

print(data)

print("="*80)

if os.path.isfile(fpath):
    f = open(fpath,"r")
    data = f.readlines()
    f.close()
else:
    print("Error: File doesn't exist!")

pp.pprint(data)

print("="*80)

with open(fpath,"r") as f:
    line = f.readline()
    while line:
        sys.stdout.write(line)
        line = f.readline()