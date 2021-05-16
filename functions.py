#The MetaData of my Favourite Song

#Initialize variables

UserAlbum = input("Which is your Micheal Jackson's favourote album: ").lower()

Album = ["dangerous", "thriller", "off the wall", "ben", "Bad", "xscape", "invincible","Forever", "immortal", "signature", "gold"]
Artist = "Micheal Jackon"
Genre = "Pop"

def userChoice():
    if UserAlbum in Album:
        
        print("Your choice:",UserAlbum.upper(),"is in the Album.")
    else:
        raise ValueError("Your input should be letters only")
        print("Oops! Not in Album")
        return
    
##userChoice()

##Tempo = "80 beats per minute"
##WrittenKey = "A major"
##Duration = 376.2
##Release_Yr = 1991
##Producer = "Micheal Jackson and Bruce Swedien"

# functions 
def album():
    print(Album)
    return

album()

def artist():
    print(Artist)
    return

artist()

def genre():
    print(Genre)
    return

genre()

def bools():
    if Genre is "Pop":
        print (True)
    else:
        print (False)
    return

bools()
