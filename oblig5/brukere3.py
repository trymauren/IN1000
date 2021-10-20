#Tar inn fornavn og etternavn, og returnerer brukernavn.
def lagBrukernavn(inputHeltnavn):
        navn = inputHeltnavn.split()
        fornavn = navn[0]
        etternavn = navn[1]
        Fetternavn = (list(etternavn)[0])
        brukernavn = fornavn + Fetternavn
        return brukernavn

#Tar inn liste over brukernavn fra lagBrukernavn og input.
#Setter dette sammen til en e-postadresse som returneres.
def lagEpost(brukernavn,inputSuffix):
    epostAdresse = brukernavn+"@"+inputSuffix
    return epostAdresse

#Printer ut en ordbok med brukernavn og epostsuffixer.
def printEpost(epostBok):
    for brukere in epostBok:
        brukernavn = brukere
        inputSuffix = epostBok[brukere]
        epostAdresse = lagEpost(brukernavn,inputSuffix)
    return epostBok

#Her det skjer...
def hovedFunksjon():
    epostBok = {}
    startprogram = input("Skriv inn i for å legge inn, p for å printe, og s for å avslutte.\n")
    while  startprogram != "s":
        if startprogram == "i":
            inputHeltnavn = input("Skriv inn fornavn og etternavn: ").lower()
            inputSuffix = input("Skriv inn e- post- suffix (eks: student.matnat.uio.no): ").lower()
            brukernavn = lagBrukernavn(inputHeltnavn) #Kjører 1. funksjon med parameter inputHeltnavn
            epostBok[brukernavn] = inputSuffix #Lager en ordbok {bruker:uio.no}
        elif startprogram == "p":
            print("\n")
            print(printEpost(epostBok))
            print(lagEpost(brukernavn,inputSuffix))
        elif startprogram == "s":
            print("Avsluttet.")
        else:
            print("Skriv inn i for å taste inn nytt navn, p for å printe, eller s for å avslutte:\n")
        startprogram = input("Skriv inn i for å legge inn, p for å printe, og s for å avslutte.\n")
hovedFunksjon()
