# Skapa en metod som tar en bokstav och returnerar true om det är en vokal och false annars.
def ifVowel(a):
    return (a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="ä" or a=="ö" or a=="å" or a=="y")
alphabet=input("Mata in bokstav: ")
print(ifVowel(alphabet))
        
