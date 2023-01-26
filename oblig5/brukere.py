
#Tar inn fornavn og etternavn, og returnerer brukernavn.
def lagBrukernavn(inputHeltnavn,brukernavnListe):
    navn = inputHeltnavn.split()
    if len(set(navn)) >= 2:
        fornavn = navn[0]
        etternavn = navn[1]
        Fetternavn = (list(etternavn)[0])
        brukernavn = fornavn + Fetternavn
        brukernavnListe.append(brukernavn)
    else:
        print("Feil")
    return brukernavnListe

#Tar inn liste over brukernavn fra lagBrukernavn og input.
#Setter dette sammen til en e-postadresse som returneres.
def lagEpost(brukernavnListe,inputSuffix):
    for i in range (len(brukernavnListe)):
        epostAdresse = brukernavnListe[i]+"@"+inputSuffix
    return epostAdresse

#Printer ut en ordbok med brukernavn og epostadresser.
def printEpost(epostBok):
    epostBok[brukernavnListe[i]]=epostAdresse
    return epostBok

def hovedFunksjon():
    epostBok = {}
    brukernavnListe = []
    brukernavn = ""
    startprogram = ""
    startprogram = input(print("Skriv inn i for å legge inn, p for å printe, og s for å avslutte.\n"))
    while  startprogram != "s":
        if startprogram == "i":
            inputHeltnavn = input(print("Skriv inn fornavn og etternavn: ")).lower()
            inputSuffix = input(print("Skriv inn suffix (eks: student.matnat.uio.no): ")).lower()
            lagBrukernavn(inputHeltnavn,brukernavnListe)
            lagEpost(brukernavnListe,inputSuffix)
            startprogram = input(print("Skriv inn i for å legge inn, p for å printe, og s for å avslutte.\n"))
        elif startprogram == "p":
            print(printEpost(epostBok))
            startprogram = input(print("Skriv inn i for å legge inn, p for å printe, og s for å avslutte.\n"))
        elif startprogram == "s":
            print("ferdig")
        else:
            print("Skriv inn i for å taste inn nytt navn, p for å printe, eller s for å avslutte:\n")


hovedFunksjon()
