from celle import Celle
from random import randint

class Spillebrett:

    def __init__(self,rader,kolonner):
        self._rader = int(rader)
        self._kolonner = int(kolonner)
        #Legger til så mange Celle- objekter i kolonner
        #innenfor def- antallet fra bruker, som igjen blir lagt i et def antall med rader
        self._rutenett = [[Celle() for antallK in range (self._kolonner)] for antallR in range (self._rader)]
        self._generasjonsnummer = 0
        self.genererer()

    def genererer(self):
        tallFra = 0 #Justerer sannsynlighet
        tallTil = 2 # --::--
        for rad in self._rutenett:
            for celle in rad:
                if randint(tallFra,tallTil) == 0:
                    celle.settLevende()#Setter tilfeldig antall celler = levende

    def tegnBrett(self): #Skriver ut spillebrettet til terminalen
        for rad in self._rutenett:
            for celle in rad:
                print(celle, end=" ")
            print()

    def finnNabo(self,denneRad,denneKolonne):
        startSok = -1 #Sjekker naboer fra og med -1
        stoppSok = 2 #til (ikke med) 2.
        naboCelleListe = [] #Her lagres alle celler som skal endres midlertidig

        for antallNaboR in range(startSok,stoppSok):
            for antallNaboK in range(startSok,stoppSok):
                naboRad     = denneRad     + antallNaboR
                naboKolonne = denneKolonne + antallNaboK

                naboJa = True

                #Denne sjekker at vi ikke er i samme celle som vi skal finne nabo for
                if naboRad == denneRad and naboKolonne == denneKolonne:
                    naboJa = False

                #Denne sjekker at vi ikke sjekker en celle som er utenfor brettet
                if naboRad <0 or naboRad >= self._rader:
                    naboJa = False

                #Denne sjekker at vi ikke sjekker en celle som er utenfor brettet
                if naboKolonne <0 or naboKolonne >= self._kolonner:
                    naboJa = False

                #Legger til sjekket celle hvis den oppfyller kravene over, med koordinater
                #tilsvarnde antallNaboK og antallNaboR
                if naboJa:
                    naboCelleListe.append(self._rutenett[naboRad][naboKolonne])

        return naboCelleListe #Returnerer liste med naboer

    def oppdatering(self):

        dodTilLevende = []
        levendeTilDod = []
        #Loop1: Looper gjennom rutenettet og henter en liste over naboer for hver celle
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):

                naboListe = self.finnNabo(rad,kolonne)
                antallLevendeNaboer = []

                #Loop3: Looper gjennom list over nabolister, og plukker ut de som er levende
                for naboCelle in naboListe:
                    if naboCelle.erLevende():
                        antallLevendeNaboer.append(naboCelle)

                celle = self._rutenett[rad][kolonne]
                statusCelle = celle.erLevende()

                if statusCelle:
                    if len(antallLevendeNaboer) <2 or len(antallLevendeNaboer) >3:
                        levendeTilDod.append(celle)

                else:
                    if len(antallLevendeNaboer) == 3:
                        dodTilLevende.append(celle)

        for celleEndre in dodTilLevende: #Legger til celler som skal komme til live i liste
            celleEndre.settLevende()
        for celleEndre in levendeTilDod: #Legger til celler som skal dø i liste
            celleEndre.settDoed()

    def finnAntallLevende(self):
        teller = 0
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                celle = self._rutenett[rad][kolonne] #Denne er viktig for å skrive ut objektene og ikke int
                if celle.erLevende():
                    teller += 1
        return teller #Returnerer antall levende celler på brettet

    def generasjonsnr(self):
        self._generasjonsnummer += 1
        return self._generasjonsnummer #Returnerer antall oppdateringer (generasjonsnr)
