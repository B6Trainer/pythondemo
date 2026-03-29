str = """’Twas brillig, and the slithy toves 
      Did gyre and gimble in the wabe: 
All mimsy were the borogoves, 
      And the mome raths outgrabe. """

words = str.split(", ")
lines = "...\n".join(words)

print("%s" % lines)

CCY = ["USD","EUR","JPY","GBP","CHF"]
Regions = ["NAM", "EMEA", "APAC", "LATAM"]
print("%s" % "USD" in CCY) # True
print("%s" % "USD" not in CCY) # False
print("%s" % (CCY + Regions)) # ['GB', 'ES', 'NL', 'F', 'D', 'I', 'P', 'SG', 'JP']
print("%s" % (Regions * 2)) # ['NAM', 'EMEA', 'APAC', 'LATAM', 'NAM', 'EMEA', 'APAC', 'LATAM']
print("%s" % (2 * Regions)) # ['NAM', 'EMEA', 'APAC', 'LATAM', 'NAM', 'EMEA', 'APAC', 'LATAM']
print("%d" % len(CCY)) # 5
print("%s" % min(CCY)) #CHF
print("%s" % max(CCY)) #USD
print("%d" % CCY.index("JPY")) # 2
print("%d" % CCY.index("JPY", 1)) # 2
print("%d" % CCY.index("GBP", 1, 4)) # 3
print("%d" % CCY.count("APAC")) # 0
print("%d" % Regions.count("APAC")) # 1

#Slicing
print("%s" % (CCY[1])) # EUR
print("%s" % (CCY[1:5])) # ['EUR', 'JPY', 'GBP', 'CHF']
print("%s" % (CCY[1:5:2])) # ['EUR', 'GBP']
print("%s" % (CCY[3:])) # ['GBP', 'CHF']
print("%s" % (CCY[:-3])) #['USD', 'EUR']


#Unpacking
CCY = ["USD","EUR","JPY","GBP","CHF"]
# Manually getting items.
a, b, c, d, e = CCY[0], CCY[1], CCY[2], CCY[3], CCY[4]
print("%s %s %s %s %s" % (a, b, c, d, e)) # USD EUR JPY GBP CHF
# Unpacking.
j, k, l, m, n = CCY
print("%s %s %s %s %s" % (j, k, l, m, n)) # USD EUR JPY GBP CHF
# Catch-all unpacking.
x, y, *z = CCY
print("%s %s %s" % (x, y, z)) # USD EUR ['JPY', 'GBP', 'CHF']


# Modifications
print("Modification")
countries = ["GB", "ES", "NL", "F"]
countries[0] = "CY"
countries[1:3] = ["US", "AU", "AT"]
countries.append("SW")
countries.extend(["YU", "ZR"])
countries.insert(1, "NI")
print("%s" % countries) # ['CY', 'NI', 'US', 'AU', 'AT', 'F', 'SW', 'YU', 'ZR']
countries.pop()
countries.pop(1)
del countries[2:4]
print("%s" % countries) # ['CY', 'US', 'F', 'SW', 'YU']
countries.remove("US")
countries.reverse()
print("%s" % countries) # ['YU', 'SW', 'F', 'CY']
copy = countries.copy()
countries.clear()
print("%s" % copy) # ['YU', 'SW', 'F', 'CY']
print("%s" % countries) # []

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
    num = 0
    while num < n:
        yield num
        num += 1
    
print("Sum using traditional function: %s" % sum(getNumsA(10)))
print("Sum using generator function: %s" % sum(getNumsB(10)))


# List comprehension
squares = [x**2 for x in range(6)]
ftemps = [32, 68, 212]
ctemps = [(f-32)*5/9 for f in ftemps]
print("squares: %s" % squares)
print("ftemps: %s" % ftemps)
print("ctemps: %s" % ctemps)

# Set comprehension
ftemps = range(0, 50, 5)
ctemps = { int((f-32)*5/9) for f in ftemps }
print("ctemps: %s" % ctemps)

# Dictionary comprehension
mydict = { i : i*i for i in range(1, 6) }
print("mydict: %s" % mydict)

def startsWithJ(element):
    if len(element) and element[0] == 'J':
        return True
    else:
        return False

def topAndTail(element):
    return "***" + element + "***"  

names = ["John", "Paul", "George", "Ringo", "Robert", "Jimmy", "John Paul", "John"]
jnames = list(filter(startsWithJ, names))
print(jnames)
sortedJnames = sorted(jnames)
print(sortedJnames)
mappedSortedJnames = list(map(topAndTail, sortedJnames))
print(mappedSortedJnames)

