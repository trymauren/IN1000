
def regnFunksjon(nedborManed,regnBok):
    for linje in nedborManed:
        deler = linje.split(",")
        maned = deler[0]
        regn = float(deler[1].rstrip())
        regnBok[maned] = regn
    return regnBok


def sammenlikning(regnBok,nedborDag):
    for linje in nedborDag:
        deler = linje.split(",")
        maneder = deler[0]
        regn = float(deler[2])
        for key in regnBok:
            if key == maneder:
                if regn > regnBok[maneder]:
                    print("Ny nedbørsrekord funnet",deler[1],deler[0],":",regn,
                    "mm, gammel nedbørsrekord var:",regnBok[maneder],"mm.")
                    regnBok[maneder]=regn
    return regnBok

def utskriftsFunksjon(regnBok,utskrift):
    for key in regnBok:
        utskrift.write(key)
        utskrift.write(" ")
        utskrift.write(str(regnBok[key]))
        utskrift.write("\n")


def hovedfunksjon():
    regnBok = {}
    nedborManed = open("max_temperatures_per_month.csv")
    nedborDag   = open("max_daily_temperature_2018.csv")
    utskrift = open("utskrift.csv","a")
    print(regnFunksjon(nedborManed,regnBok)) #Printer ordbok med måned/nedbør
    print(sammenlikning(regnBok,nedborDag))
    utskriftsFunksjon(regnBok,utskrift)
hovedfunksjon()
