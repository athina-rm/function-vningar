# Skapa en metod som du döper till HittaLangstaOrdet. Metoden skall ta som inparameter en array
#med strängar. Metoden skall loopa igenom arrayen och returnera det längsta ordet.

def findLongestWord(a):
    long=a[0]
    for i in a:
        if len(long)<=len(a[i]) :
            long=a[i]
    return long

wordArray=[]
count=int(input("no.of words:"))
for i in range (0,count):
    wordArray.append(input("mata in ord:"))
print (findLongestWord(wordArray))
