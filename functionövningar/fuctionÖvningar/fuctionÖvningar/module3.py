# Skapa en metod som räknar ut hur mycket momsen blir på en viss summa. Summan skall vara en inparameter av typen 
# int. Metoden skall returnera momsvärdet
def calcVat(s):
    return(.2*s/1.2)
summa=float(input("Ange summan : "))
print(calcVat(summa))
