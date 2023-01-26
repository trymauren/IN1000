from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():
    min_liste = Spilleliste("Tryms liste")
    sang1 = Sang("Adagio","Albinoni","adagio.wav")
    sang2 = Sang("Ode to Joy","Beethoven","ode_to_joy.wav")
    min_liste.leggTilSang(sang1)
    min_liste.leggTilSang(sang2)
    min_liste.spillAlle()
hovedprogram()
