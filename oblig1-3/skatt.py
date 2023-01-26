inntekt=float(input("Skriv inn inntekt:\n")) #Leser input (inntekt)
if(inntekt<10000):
    skatt=inntekt*0.1 #Beregner skatt av inntekt under 10000
else:
    skatt=10000*0.1+(inntekt-10000)*0.3 #Beregner skatt av inntekt f.o.m. 10000
print("Skatt:", skatt)
