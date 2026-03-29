
#from Functions import SimpleFunctions

from PythonDataTypes.utils.messages import *


print("--"*20+" This is the scratchpad file."+"--"*20)

#Generators
# Return a collection of numbers.
def getNumsA(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Equivalent effect using a generator.
def getNumsB(n):
    num = 5
    while num < n:
        yield num
        num += 1
    
print("Sum using traditional function: %s" % sum(getNumsA(10)))
print("Sum using generator function: %s" % sum(getNumsB(10)))


g = getNumsB(4)

print(next(g))  # 5
print(next(g))  # 6