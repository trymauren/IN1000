def prosedyre():
    alder=int(input("Skriv inn alder for å regne ut billettpris:\n"))
    billettpris=0

    if(alder<17 or alder==17): print("Billetten koster 30 kroner.")

    elif(alder>63): print("Billetten koster 35 kroner.")

    else: print("Billetten koster 50 kroner.")

prosedyre()
