#Skapa ett program med en ny metod. Metoden skall ta emot två inparametrar av typen string och
#slå ihop dom till en sträng och returnera det nya värdet. Anropa den nya metoden från Main och
#skriv ut resultatet på skärmen.

def stringConcat(string1,string2):
    return(string1+string2)

string1=input("Ange första string: ")
string2=input("Ange andra string: ")
fString=stringConcat(string1,string2)
print(fString)

