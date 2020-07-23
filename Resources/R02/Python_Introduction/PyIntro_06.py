import sys
import os

# PyInto Lesson 06
# If statements
# Code blocks

if len(sys.argv) < 3:
    print("Error: we need at least two params!")
    print("Example: python PyIntro_06.py <int> <int>")
    sys.exit(0)
else:
    # you have two params

    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])

    if p1 > p2:
        print(f"{p1} is greater than {p2}")
    elif p2 > p1:
        print(f"{p2} is greater than {p1}")
    else:
        print(f"{p2} is equal than {p1}")