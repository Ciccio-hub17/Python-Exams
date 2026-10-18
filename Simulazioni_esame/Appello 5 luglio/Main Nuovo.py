from operator import itemgetter

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
        efficienza = float(parti[2])
        for orario in abitazioni[idAbitazione]:
            abitazioni[idAbitazione][orario].append (dimensione)
            abitazioni[idAbitazione][orario].append (efficienza)
    
    for line in inFileMeteo:
        parti = line.split (";")
        orario = parti[1]
        sole = float(parti[2])
        for idAbitazione in abitazioni:
            abitazioni[idAbitazione][orario].append (sole)

    inFileConsumi.close ()
    inFileImpianti.close()
    inFileMeteo.close()

    return abitazioni

def calcolo (abitazioni):
    #consumo, dimensione, efficienza, sole
    energiaProdotta = 0
    energiaConsumata = 0
    energiaAutoconsumata = 0
    energiaImmessaInRete = 0

    dictAutoconsumo = dict ()
    dictAutoefficienza = dict ()
    for idAbitazione in abitazioni:
        energiaProdottaCasa = 0
        energiaConsumataCasa = 0
        energiaAutoconsumataCasa = 0
        for orario in abitazioni[idAbitazione]:
            lista = abitazioni[idAbitazione][orario]
            efficienza = lista[2]
            dimensione = lista[1]
            sole = lista[3]
            consumo = lista[0]

            energiaProdottaCasa = energiaProdottaCasa + efficienza * dimensione * sole
            energiaConsumataCasa = energiaConsumataCasa + consumo

        energiaProdotta = energiaProdotta + energiaProdottaCasa
        energiaConsumata = energiaConsumata + energiaConsumataCasa

        differenzaEnergia = energiaProdottaCasa - energiaConsumataCasa

        if differenzaEnergia > 0:
            energiaAutoconsumataCasa = energiaConsumataCasa
            energiaAutoconsumata = energiaAutoconsumata + energiaConsumataCasa
            energiaImmessaInRete = energiaImmessaInRete + differenzaEnergia

        else:
            energiaAutoconsumataCasa = energiaProdottaCasa
            energiaAutoconsumata = energiaAutoconsumata + energiaProdottaCasa

        dictAutoconsumo[idAbitazione] = energiaAutoconsumataCasa
        dictAutoefficienza[idAbitazione] = energiaAutoconsumataCasa
        
    print ("Report aggregato")
    print (f"Energia Prodotta: {energiaProdotta:.2f} kwh")
    print (f"Energia Consumata: {energiaConsumata:.2f} kwh")
    print (f"Energia Autoconsumata: {energiaAutoconsumata:.2f} kwh")
    print (f"Energia Immessa in rete: {energiaImmessaInRete:.2f} kwh")

    autoconsumo = energiaAutoconsumata / energiaProdotta * 100
    autoefficienza = energiaAutoconsumata / energiaConsumata * 100

    print (f"Autoconsumo: {autoconsumo:.2f}%")
    print (f"Autoefficienza: {autoefficienza:.2f}%")

    for id in dictAutoconsumo:
        dictAutoconsumo[id] = dictAutoconsumo[id] / energiaProdotta
    
    for id in dictAutoefficienza:
        dictAutoefficienza[id] = dictAutoefficienza[id] / energiaConsumata

    dictAutoconsumo = sorted (dictAutoconsumo.items(), key =itemgetter (1), reverse = True )
    dictAutoefficienza = sorted (dictAutoefficienza.items(), key = itemgetter(1), reverse = True)

    print ("Le tre abitazioni che hanno il più alto autoconsumo sono", end = ": ")
    for i in range (3):
        print (dictAutoconsumo[i][0], end = " ")
    
    print ()
    print ("Le tre abitazioni con la più alta autoefficienza sono", end = ": ")
    for i in range (3):
        print (dictAutoefficienza[i][0], end = " ")

def main ():
    abitazioni = leggiFile ("consumi.txt", 'impianti.txt', 'meteo.txt')
    calcolo (abitazioni)

main ()