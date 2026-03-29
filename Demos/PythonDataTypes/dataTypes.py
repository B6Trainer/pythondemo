#int
print('--- INT --- ')
x = 1
print(x)
print(type(x))
x = 10000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))


#float
print('--- FLOAT --- ')
f = 3.2e4 + 0.00002e-6
formatString = "%16.20g"
print(formatString % f)
print(type(f))

#complex
print('--- COMPLEX --- ')
c1 = 1j
c2 = 2j
c3 = c1 * c2
print(c3)
print(type(c3))
print(c3.real)
print(c3.imag)


# Strings
print('--- STRINGS --- ')
x = 'Good'
y = " day"
print(x + y)
z = """
Hello
World
"""
print(z)
print(type(z))
print(z.upper())


# Lists
print('--- LISTS --- ')
list1 = []
list2 = [4]
list3 = [2, 4, 6]
list4 = [1, "two", 3, 'four']
list5 = [ [2, 3], [6, 8]]
print(type(list5))
print(list1, ': ', len(list1))
print(list2, ': ', len(list2))
print(list3, ': ', len(list3))
print(list4, ': ', len(list4))
print(list5, ': ', len(list5))

# more lists
print('--- MORE LISTS --- ')
list3 = [2, 4, 6]
print(list3[1])
print(list3[-1])
print(list3[0:2])
list1.append(8)
print(list1)
list1.extend([10, 12])
print(list1)
list1.insert(2, 7)
print(list1)

# and more lists
print('--- AND MORE LISTS --- ')
list7 = [2, 3, 6, 8]
print(list7.index(8))
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6.index('a'))
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6.pop())
print(list6)
print(list6.pop(0))
print(list6)
list6.remove('Upon')
print(list6)

#tuples
print('--- TUPLES --- ')
tup1 = (1, 3, 5, 7)
print('tup1[2]:\t', tup1[2])
print('tup1[1:3]:\t', tup1[1:3])
print('len(tup1):\t', len(tup1))
#Notice the slice is also a tuple

#ranges
print('--- RANGES --- ')
for i in range(1, 10, 2):
    print(i, ' ', end='' )
print()
for i in range(10, 1, -2):
    print(i, ' ', end='')

# List comprehension
print('--- LIST COMPREHENSION --- ')
list1 = [1, 2, 3, 4, 5,6]
print('list1: ', list1)

list2 = [e+1 for e in list1]
print('list2: ', list2)

first9squares = [ x * x for x in range(1,10,1) ]
print('first9squares: ', first9squares)


# dictionaries
print('--- DICTIONARIES --- ')
d = {'one':1, 'two':2}
print(d)
print(type(d))
print(d['two'])
d['three'] = 3
print(d)
del d['two']
print(d)
seasons = { "Spring":("Mar", "Apr", "May"),
             "Winter":("Dec", "Jan", "Feb") }
print(seasons["Spring"])
print(seasons["Spring"][1])

# more dictionaries
print('--- MROE DICTIONARIES --- ')
print(d.keys())
print(d.values())
values = d.values()
for e in values:
    print(e)


# and more dictionaries
print('--- AND MROE DICTIONARIES --- ')
d['four'] = 4
print(d.keys())
print(sorted(d.keys()))
l = ["%s=%s" % (k, v) for k, v in d.items()]
print(l)

#None Type
print('--- NONE TYPE --- ')
var = 100
print(type(var))
var = None
print(type(var))
if var is None:
    print("var is null")

    



