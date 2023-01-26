tall = ""
liste = []
while tall != 0: #Bruker legger til tall helt til input==0,
    tall = int(input("Skriv inn tall:\n"))#da avbrytes løkken
    liste.append(tall)

print("\n")

for i in range(len(liste)): #Printer alt innholdet i liste
    print(liste[i])

minSum=0

for i in liste: # Regner ut summen av innholdet i liste
    minSum=minSum+i

print("\nSummen av tallene er:",minSum)

storst=liste[0] #Finner det største tallet
for e in liste:
    if e>storst:
        storst=e

print("Det største tallet er:",storst)

minst=liste[0] #Finner det minste tallet
for a in liste:
    if a<minst:
        minst=a

print("Det minste tallet er:",minst)
