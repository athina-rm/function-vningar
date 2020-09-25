# Skapa ett program där användaren får en fråga om att mata in sin ålder. Skapa en metod som tar
#emot det inmatade värdet och kontrollerar om användaren är myndig dvs över 18 år. Metoden
#returnerar sant eller falskt. Anropa metoden och skriv ut på skärmen om användaren är myndig eller ej.
def ifAdult(a):
    return(a>=18)   
       
age=int(input("Mata in ålder : "))
if ifAdult(age):
    print("Myndig")
else:
    print("inte myndig")

