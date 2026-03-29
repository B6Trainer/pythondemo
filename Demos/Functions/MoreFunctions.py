def ChooseSong(song="Blowin in the wind", artist="Bob Dylan"):
    print("\nPlaying %s by %s" % (song, artist))

# Usage (i.e. client code)
ChooseSong("Blowin in the wind", "Peter, Paul and Mary")
ChooseSong("Jokerman")
ChooseSong()

def Somethings(name, *things):
    print("Somethings for %s" % name)
    for thing in things:
        print(" %s" % thing)

Somethings("Pat", "Razor", "Toothbrush", 2.4, "Deoderant", 3, "Mouthwash")


ChooseSong(song="Blowin in the wind", artist="Peter, Paul and Mary")
ChooseSong(artist="Joni Mitchell", song="Big Yellow Taxi")
ChooseSong("Blowin in the wind", artist="Peter, Paul and Mary")

def printer(*args):
    print("Args:", args)
    
a = (1, 2, 3, 4)
b = [1, 2, 3, 4]

printer(0, 1, 2, 3, 4, 5)
printer(0, a, 5)
printer(0, b, 5)
printer(0, *a)
printer(0, *b)
printer(0, *[1,2,3,4])
