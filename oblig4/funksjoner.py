##Regner ut summen av to tall
#@sum regner ut summen av de to tallene
#@returnerer summen av de to tallene
def sumTall(tall1,tall2):
     sum = tall1+tall2
     return sum

resultat1 = sumTall(2,4)
resultat2 = sumTall(450,3984081)
print("Summen av tallene er",resultat1)
print("Summen av tallene er",resultat2)

inputStreng = input("Skriv inn et ord:\n")
inputBokstav = input("Skriv inn bokstav:\n")

##Finner antall av en bokstav i en streng
#@antall sjekker antall forekomster
#@returnerer antallet forekomster
def sjekkBokstav(inputStreng,inputBokstav):
    antall=inputStreng.count(inputBokstav)
    return antall

antall = sjekkBokstav(inputStreng,inputBokstav)
print("Bokstaven",inputBokstav,"forekommer",antall,
"ganger i strengen",inputStreng)
