from spillebrett import Spillebrett

def hovedprogram():

    rad = input("Skriv inn lengde på spillebrettet: ")
    kolonne = input("Skriv inn bredde på spillebrettet: ")

    sb1 = Spillebrett(rad,kolonne)
    sb1.tegnBrett()
    print("Det er "+(str(sb1.finnAntallLevende())+" levende celler."))
    print("Gennr: "+(str(sb1.generasjonsnr())))

    valg = ""
    while valg!= "q":
        valg = input("Trykk enter for å fortsette, eller trykk Q for å avslutte: ").lower()
        sb1.oppdatering()
        sb1.tegnBrett()
        print("Det er "+(str(sb1.finnAntallLevende())+" levende celler."))
        print("Gennr: "+(str(sb1.generasjonsnr())))
        if sb1.generasjonsnr() > 1000:
            valg = "q"
hovedprogram()
