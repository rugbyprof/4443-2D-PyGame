import sys
import os

# PyIntro Lesson 07
# Boolean Operators: < > <= >= != ==
# Logical operators: and or
# Logical Reversal: not

if len(sys.argv) < 4:
    print("Error: we need at least two params!")
    print(f"Example: python {__file__} <int> <int> <int>")
    sys.exit(0)
else:
    # you have two params so proceed

    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])
    p3 = int(sys.argv[3])

    if not (p1 > p2 and p1 > p3):
        print(f"{p1} is the biggest")


