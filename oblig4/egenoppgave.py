"""Skriv en oppgave der bruker kan skrive inn ulike personers
bursdagsdatoer. Informasjonen skal lagres i en ordbok, og
bruker skal så ha mulighet til å hente ut en persons bdato."""

antallVenner = int(input("Hvor mange venner har du?\n"))
bursdagsBok = {}
##Legger inn navn og dato i en ordbok
#@Løkke tilegner navn til key og dato til value
#@returnerer ordboka
def inputProsedyre(antallVenner):
    for noe in range (antallVenner):
        vennNavn = input("Skriv inn navn på person:\n")
        vennDato = input("Skriv inn fødselsdato på person:\n")
        bursdagsBok[vennNavn] = vennDato
    return bursdagsBok
inputProsedyre(antallVenner)

##Slår opp i ordboka fra inputProsedyre
#@Henter inn streng fra bruker
#@Printer ut dato tilhørende strengen
def inputProsedyre(bursdagsBok):
    navnInput=input("Skriv inn navn på person du vil vite bursdag til:\n")
    print(navnInput,"har bursdag",bursdagsBok[navnInput])

inputProsedyre(bursdagsBok)
