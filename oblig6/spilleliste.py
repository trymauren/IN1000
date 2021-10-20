from sang import Sang

class Spilleliste:
    #Konstruerer spilleliste- objekt bestående av et navn og en liste
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #Leser inn sanger fra txt-fil og lager Sang- objekter ut av dem.
    #Disse blir lagt til i spillelista
    def lesFraFil(self,filnavn):
        fil = open(filnavn)
        for linje in fil:
            alle_data = linje.strip().split(";")
            tittel = alle_data[0]
            artist = alle_data[1]
            nySang = Sang(artist,tittel)
            self._sanger.append(nySang)
        fil.close()

    #Legger til nytt Sang- objekt i spilleliste
    def leggTilSang(self,nySang):
        alle_data = nySang.strip().split(";")
        leggtil_sang = Sang(alle_data[0],alle_data[1])
        self._sanger.append(leggtil_sang)

    #Fjerner sang- objekt
    def fjernSang(self,sang):
        (self._sanger).remove(sang)

    #Printer ut hvilken sang som spilles. Pga __str__ printes den på fint format
    def spillSang(self,nySang):
        print(nySang)

    #Printer at alle sanger spilles.
    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    #Sjekker om en tittel er i spilleliste. Hvis den er det, returneres den
    def finnSang(self,tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel) == True:
                return sang

    #Returnerer alle sanger av spesifisert artist
    def hentArtistUtvalg(self,artistnavn):
        sangliste = []
        for sang in self._sanger:
            if(sang.sjekkArtist(artistnavn)):
                sangliste.append(sang)
        return sangliste
