print("Numbers from 1-5 inclusive")
i = 1
while i <= 5:
    print(i)
    i = i + 1

lottonumbers = [2, 7, 3, 12, 19, 1]
for item in lottonumbers:
    print(item)
    
print("Numbers from 0-4 inclusive")
for i in range(5):
    print(i)
    
print("Numbers from 6-10 inclusive")
for i in range(6, 11):
    print(i)
    
print("First 5 odd numbers")
for i in range(0, 9, 2):
    print(i + 1)
    
magicnumber = int(input("What is the magic number? "))
print("This loop terminates if it hits the magic number")
for i in range(1, 21):
    if i == magicnumber:
            break
    print(i)
print("End")

print("\nThis loop skips the magic number")
for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
print("End")


magicnumber = int(input("What is the magic number? "))
print("This loop does some processing if it doesn't detect the magic number")
for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)
else:
    print("The magic number %d was not detected" % magicnumber)
print("End")


while True:
    exammark = int(input("Enter a valid exam mark: "))
    if exammark >= 0 and exammark <= 100:
        break
print("Your exam mark is %d" % exammark)