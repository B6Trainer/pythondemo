def SayHelloWorld():
    print("Hello")
    print(" ")
    print("World")
    
def SayGoodbyeWorld():
    print("Goodbye")
    print(" ")
    print("World")
    
SayHelloWorld()
SayGoodbyeWorld()



def SayAnything(message1, message2):   
    print(message1 + " " + message2)
    
SayAnything("Hello", "World")
SayAnything("Goodbye", "World")

def SayAlot(message1, message2, count):   
    for i in range(count):
            print(message1 + " " + message2)
        
SayAlot("Hello", "World", 3)
SayAlot("Goodbye", "World",2)

def GenerateMessage(message1, message2):
    return message1 + " " + message2

message = GenerateMessage("John", "Lennon")
print("Fav beatle is %s" % message)

def makeAList(start,end):
    newList = list(range(start,end))
    return newList

def dictionary():
    return {'one' : 1, 'two' : 2}

list1 = makeAList(5, 10)
print(list1)

def getData(symbol):
    open = 123
    close = 95
    longname = 'Facebook'
    increased = open < close

    return longname, open, close, increased

name, open, close, rose = getData('FB')

print(name)
print(open)
print(close)
print(rose)

def swap(a, b):
    return b, a
a = 42
b = 54

x, y = swap(a, b)
print(x, ', ', y)
print('')
z = swap(a, b)
print(z)
