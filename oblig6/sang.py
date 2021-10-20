#import simpleaudio as sa

class Sang:
        #Konstruerer Sang- objekt, bestående av en artist og en tittel
    def __init__(self,artist,tittel):
        self._artist = artist
        self._tittel = tittel

        #Gjør om formatet når det brukes print eller str på Sang- objekter til
        #brukervennlig format
    def __str__(self):
        return (self._tittel+", av "+self._artist)

        #Skriver ut tittel og artist på sang
    def spill(self):
        #wave_obj = sa.WaveObject.from_wave_file(self._tittel)
        #play_obj = wave_obj.play()
        #play_obj.wait_done()
        print("Spiller " + self._tittel + " av " + self._artist)

    #Sjekker om artist satt inn er lik artist til spillende sang
    def sjekkArtist(self,navn):
        #Deler opp strengene på mellomrom, og sjekker om de deler noen elementer
        artistnavn_liste = (self._artist.lower()).split(" ")
        inputartistnavn_liste = (navn.lower()).split(" ")
        for artist in artistnavn_liste:
            for inputartist in inputartistnavn_liste:
                if artist == inputartist:
                    return True
        return False

        #Sjekker tittel skrevet inn er lik tittel til spillende sang
    def sjekkTittel(self,intittel):
        if intittel.lower() == (self._tittel.lower()):
            return True
        return False

        #Sjekker at både tittel og artist skrevet inn er likt som spillende sang
    def sjekkArtistOgTittel(self,navn,intittel):
        if self.sjekkArtist(navn) and self.sjekkTittel(intittel):
            return True
        return False
