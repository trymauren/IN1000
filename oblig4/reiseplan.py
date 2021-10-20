#Legger til 5x bruker-input i en liste
steder=[]
for i in range(5):
    reisemal=input("Skriv inn reisemål:\n")
    steder.append(reisemal)

#Legger til 5x bruker-input i en liste
klesplagg=[]
for e in range(5):
    kler=input("Skriv inn klesplagg:\n")
    klesplagg.append(kler)

#Legger til 5x bruker-input i en liste
avreisedatoer=[]
for a in range(5):
    dato=input("Skriv inn avreisedato:\n")
    avreisedatoer.append(dato)

#Legger til de 3 listene over i en ny liste
reiseplan=[]
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

#Printer ut den nøstede listen
for i in range (len(reiseplan)):
    print(reiseplan[i])

#Tar inn 2x brukerinput og skriver ut verdien de tilsvarer
i1=int(input("Skriv inn tall:\n"))
i2=int(input("Skriv inn tall:\n"))

if(i1<3 and i2<6):
    print(reiseplan[i1][i2])
else:
    print("Indeksen(e) er ikke i lista")
