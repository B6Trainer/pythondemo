squares = [x**2 for x in range(6)]
ftemps = [32, 68, 212]
ctemps = [(f-32)*5/9 for f in ftemps]
print("squares: %s" % squares)
print("ftemps: %s" % ftemps)
print("ctemps: %s" % ctemps)


ftemps = range(0, 50, 5)
ctemps = { int((f-32)*5/9) for f in ftemps }
print("ctemps: %s" % ctemps)

mydict = { i : i*i for i in range(1, 6) }
print("mydict: %s" % mydict)