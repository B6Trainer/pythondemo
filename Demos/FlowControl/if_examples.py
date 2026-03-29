age = int(input("Enter your age: "))
gender = input("Enter gender [M/F]: ").lower()

if age < 18:
    if gender == "m":
        print("Boy")
    else:
        print("Girl")
else:
    if gender == "m":
        print("Man")
    else:
        print("Woman")
        

if gender == "m":
    isMale = True
else:
    isMale = False

togo = (65 - age) if isMale else (60 - age)
print("%d years to retirement" % togo)

beatle = input("Who is your favourite beatle? ")
if beatle == "Ringo":
    pass # Really !!
print("Your favourite beatle is %s " % beatle)


country = input("Please enter your country: ")
if country in ("Brazil", "Russia", "India", "China"):
    print("BRIC country")
elif country in ("Kenya", "Tanzania", "Rwanda"):
    print("East African country")
elif country in ("England", "Scotland", "Wales", "Northern Ireland"):   
    print("UK country")
else:
    print("%s isn't classified in this particular application!" % country)
    

number = int(input("Enter a football jersey number [1 to 11]: "))
if number == 1:
    print("Goalie")
elif number in range(2, 6):
    print("Defender")
elif number in range(6, 10):
    print("Midfielder")
else:
    print("Striker")