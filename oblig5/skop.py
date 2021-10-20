def minFunksjon():
    for x in range (2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()

"""Programmet definerer først funksjonen minFunksjon, deretter funksjonen
hovedprogram. Ingen av funksjonene har parametere. Videre kalles funksjonen
hovedprogram. I denne blir variablen a definert til = 42 og variabelen b til
= 0. Så printes b (printen blir 0). Videre blir b = a, altså b = 42.
a blir så definert til å være lik minFunksjon. Deretter printes b (printen
blir 42), før a printes helt til slutt i funksjonen. [Da kalles minFunksjon,
hvor programmet itererer gjennom verdier opp til og med 2. Videre defineres
en ny variabel c til å være = 2, før c printes (printen blir 2). Samtidig øker
verdien tilegnet c med 1. Videre innføres en ny (lokal) variabel b, som blir
satt til = 10. Videre økes verdi til b med a, men a er ikke definert, og
det vil dukke opp en feilmelding. Hadde a vært definert i funksjonen på forhånd,
ville programmet fortsatt, og funksjonen hadde printet b (print = 10), b=10
hadde også blitt returnert. Videre printer funksjonen b, altså 42, og til slutt
printer den a, som er lik den returnerte verdien fra minFunksjon, altså 10."""
