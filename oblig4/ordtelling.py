##Regner ut lengden på input og skriver ut
def antallBokstaver():
    ordInn = input("Skriv inn et ord:\n")
    lengdeOrd=(len(ordInn))
    print(lengdeOrd)
antallBokstaver()

tekst=input("Skriv inn tekst:\n")
ordene = tekst.split()
##Lager en ordbok og returnerer denne
#@Løkke tilegner ord til key/ antall til value i ordboka "teller"
#@returnerer ordboka
def ord_teller(tekst):
    teller = dict()

    for ord in ordene:
        if ord in teller:
            teller[ord] += 1
        else:
            teller[ord] = 1

    return teller

ord_teller(tekst)

print(ord_teller(tekst)) #Printer ordboka

print("Det er",len(ordene),"ord i setningen din.")
#Løkke for å skrive ut. Bruker if- test for å bestemme "gang"/"ganger"
for element in ord_teller(tekst): #, etter hvor mange ganger ordet forekommer

    lengdeOrd = len(str(element))

    if (ord_teller(tekst)[element]) == 1:
        print("Ordet",str(element),"forekommer",
        str(ord_teller(tekst)[element]),"gang, og har",lengdeOrd,"bokstaver.")
    else:
        print("Ordet",str(element),"forekommer",
        str(ord_teller(tekst)[element]),"ganger, og har",lengdeOrd,"bokstaver.")
