input1=int(input("Skriv inn tall: "))
input2=int(input("Skriv inn tall: "))
def addisjon(tall1,tall2):
    sum = tall1+tall2
    return sum
print("Resultatet av summen blir:",int(addisjon(input1,input2)))

def subtraksjon(tall1,tall2):
    sub = tall2-tall1
    return sub
print("Resultatet av subtraksjonen blir:",int(subtraksjon(input1,input2)))

def divisjon(tall1,tall2):
    dividend = tall1/tall2
    return dividend
print("Resultatet av divisjonen blir:",int(divisjon(input1,input2)))

input3=int(input("Skriv inn tommer for å renge om til cm: "))
def tommerTilCm(antallTommer):
    assert antallTommer>0
    return antallTommer*2.54
print(input3,"tommer blir:",float(tommerTilCm(input3)),"cm.")
