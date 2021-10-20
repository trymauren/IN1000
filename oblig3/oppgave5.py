#Lag et program der bruker kan legge inn allergier og
#Få ut en oversikt over matvarer som bør unngås

allergiSet=set()

def allergiProsedyre():
    allergi=input("Legg til allergi:")
    allergiSet.add(allergi) #Legger til en allergi i mengden

allergiProsedyre()
allergiProsedyre()
allergiProsedyre()
allergiProsedyre()

print("Følgende matvarer bør unngås:")
for key in allergiSet: #Printer ut allergi mer oversiktlig
    print(key)
