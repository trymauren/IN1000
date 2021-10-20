liste=[1,2,3]
liste.append(4)
print(liste)

liste2=[]
liste2.append(input("Legg til navn:\n"))
liste2.append(input("Legg til navn:\n"))
liste2.append(input("Legg til navn:\n"))
liste2.append(input("Legg til navn:\n"))

if "Trym" in liste2:
    print("Du husket meg!\n")
else:
    print("Du glemte meg!\n")

sum = 0
produkt = 1
for element in liste:
    sum += element
    produkt *= element

print("Summen av lista er:",sum,". Produktet av lista er:",produkt,".")

del liste[-2:]
print(liste)
