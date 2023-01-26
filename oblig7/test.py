

hovedliste = []
delliste1 = ["a","b","c"]
delliste2 = ["6","5","4"]
delliste3 = ["heidi","kari","maria"]

hovedliste.append(delliste3)
hovedliste.append(delliste2)
hovedliste.append(delliste1)

for g in hovedliste:
    for y in g:
        print(y)
print()
print(hovedliste[0][1])
