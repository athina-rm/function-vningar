# Skriv en metod som du döper till Translate() . Den skall översätta en text till "rövarspråket". Det
#betyder att dubbla varje konsonant och placera bokstaven ”o” mellan dessa konsonanter. Till
#example , Translate("this is fun") skall returna strängen "tothohisos isos fofunon". 
def translate(a):
    for i in range (0,len(a)):
        if (a[i]!="a" or a[i]="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="ä" or a[i]=="ö" or a[i]=="å" or a[i]=="y")
Sentence=input("Mata in meningen: ")
print(translate(Sentence))
