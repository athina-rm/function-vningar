# Skapa två metoder , en som heter sum() och en som heter multiply() . Dessa skall summera
#respektive multiplicera alla tal I en lista av heltal.Till exempel , sum([1,2,3,4]) skall returnera 10,
#och multiply([1,2,3,4]) skall returna 24. @
def sum(a):
    s=0
    for i in range (0,len(a)):
        s+=a[i]
    return s

def multiply(a):
    s=1
    for i in range (0,len(a)):
        s*=a[i]
    return s

numArray=[]
count=int(input("Mata in count : "))
for i in range (0,count):
    numArray.append(int(input(f"Mata in tal{i+1}: ")))
print("Sum = ",sum(numArray))
print("product = ",multiply(numArray))

