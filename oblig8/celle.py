class Celle:
#konstruerer
    def __init__(self):
        self._status = "død"

    def __str__(self):
        return self.hentStatusTegn()

#endre status
    def settDoed(self):
        self._status = "død"

#endre status
    def settLevende(self):
        self._status = "levende"

#sjekkomlevende

    def erLevende(self):
        if self._status == "levende":
            return True
        return False

#sjekkomlevende string output
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        return "."
