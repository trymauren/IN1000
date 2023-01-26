#Leser av 2 datoer lagt inn av bruker
datodag1=input("Oppgi dag i første dato ")
datomaned1=input("Oppgi måned i første dato ")
datodag2=input("Oppgi dag i andre dato ")
datomaned2=input("Oppgi måned i andre dato ")
if(datomaned1>datomaned2):
    print("Feil rekkefølge") #Hvis første måned kommer etter andre måned, stopper if- test og skriver ut
elif(datomaned1<datomaned2):
    print("Riktig rekkefølge") #Hvis første måned kommer før andre måned, stopper if- test og skriver ut
else:                           # Hvis måned = måned, går testen videre for å sjekke dag mot dag
        if(datodag1>datodag2):
            print("Feil rekkefølge") #Hvis første dag kommer etter andre dag, stopper if- test og skriver ut
        elif(datodag1<datodag2):
            print("Riktig rekkefølge") #Hvis første dag kommer før andre dag, stopper if- test og skriver ut
        else:
            print("Samme dato!") #Hvis dag = dag, stopper if- test og skriver ut
