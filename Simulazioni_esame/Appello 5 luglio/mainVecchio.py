def leggiFile (consumi, impianti, meteo):
    inFileConsumi = open (consumi, "r")
    inFileImpianti = open (impianti, "r")
    inFileMeteo = open (meteo, "r")


    abitazioni = dict ()

    next (inFileImpianti)
    next (inFileConsumi)
    next (inFileMeteo)
    #ID1;01/01/2023;00:00;1.86

    for line in inFileConsumi:
        dictOra = dict ()
        parti = line.split (";")
        idAbitazione = parti[0]
        ora = parti[2]
        consumo = float(parti[-1])

        if idAbitazione not in abitazioni:

            dictOra [ora] = [consumo]
            abitazioni [idAbitazione] = dictOra

        else:
            
            abitazioni[idAbitazione][ora] = [consumo]

    for line in inFileImpianti:
        parti = line.split (";")
        idAbitazione = parti[0]
        dimensione = float(parti[1])
        efficienza = float (parti[2])

        dizionarioOrari = abitazioni[idAbitazione]
        for orario in dizionarioOrari:
            dizionarioOrari[orario].append (dimensione)
            dizionarioOrari[orario].append (efficienza)

    for line in inFileMeteo:
        parti = line.split (";")
        ora = parti[1]
        sole = float(parti[-1])
        for abitazione in abitazioni:
            abitazioni[abitazione][ora].append (sole)

    # abitazione = 
    # ora = consumo, dimensione, efficienza, sole
    inFileConsumi.close()
    inFileImpianti.close ()
    inFileMeteo.close()
    
    return abitazioni


def calcolo (abitazioni):
    print ("Report aggregato")

    energiaProdotta = 0
    energiaConsumata = 0
    energiaAutoconsumata = 0

    for abitazione in abitazioni:
        energiaProdottaCasa = 0
        energiaConsumataCasa = 0
        for ora in abitazione:
            consumo = abitazioni[abitazione][ora][0]
            efficienza = abitazioni[abitazione][ora][2]
            dimensione = abitazioni[abitazione][ora][1]
            sole = abitazioni[abitazione][ora][3]
            energiaProdottaCasa = energiaProdottaCasa + efficienza * dimensione * sole
            energiaConsumataCasa = energiaConsumataCasa + consumo
        
        differenza = energiaProdottaCasa - energiaConsumataCasa

        energiaProdotta = energiaProdotta + energiaProdottaCasa
        energiaConsumata = energiaConsumata + energiaConsumataCasa    

    print (f"Energia Prodotta: {energiaProdotta} kw")
    print (f"Energia Consumata: {energiaConsumata} kw")
    print (f"Energia immessa in rete: {energiaProdotta-energiaConsumata} kw")    

def main ():
    abitazioni = leggiFile ("consumi.txt", 'impianti.txt', 'meteo.txt')
    calcolo (abitazioni)


main ()
