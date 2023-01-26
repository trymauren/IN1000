#Lag en quiz hvor bruker må svare på 3 spørsmål.
#Programmet skal telle poeng, og quizen avsluttes ved første feil svar/
#når det er tomt for spørsmål.

stad1=input("Hva er hovedstaden i Norge?")

poeng=0

if(stad1=="Oslo"):
    poeng=poeng+1
    stad2=input("Hva er hovedstaden i Sverige?")

    if(stad2=="Stockholm"):
        poeng=poeng+1
        stad3=input("Hva er hovedstaden i Danmark?")

        if(stad3=="København"):
            poeng=poeng+1
            print("Du fikk 3 poeng.")

        else:print("Du fikk 2 poeng.")

    else:print("Du fikk 1 poeng.")

else:print("Du fikk 0 poeng.")
