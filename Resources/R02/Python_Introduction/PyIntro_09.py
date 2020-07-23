import sys
import os

# PyIntro Lesson 09
# Lists (part 1)

lst2 = [1,2,3,4,5]
lst1 = [10,11,12]

lst1.append(6)
lst1.extend(lst2)

lst3 = list(lst1)

lst3[0] = 99

# p = lst1.pop(0)

# lst1.sort()

# print(lst1)

# lst1.reverse()

# print(lst1)

# lst1.remove(11)

print(lst1)
print(lst3)



# for item in lst:
#     print(item)