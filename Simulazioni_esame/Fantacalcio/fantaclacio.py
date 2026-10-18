BUDGET = 260

def leggiFile (filename):
    portieri = []
    difensori = []
    centrocampisti = []
    attaccanti = []
    infile = open (filename, "r")

    for line in infile:
        line = line.strip().split (", ")
        nome = line[0]
        ruolo = line[2]
        quotazione = int (line[3])
        if ruolo == "portiere":
            portieri.append ((nome, quotazione))
        elif ruolo == "difensore":
            difensori.append ((nome, quotazione))
        elif ruolo == "centrocampista":
            centrocampisti.append ((nome, quotazione))
        else:
            attaccanti.append ((nome, quotazione))

    infile.close ()
    return portieri, difensori, centrocampisti, attaccanti

def gioco (portieri, difensori, centrocampisti, attaccanti):
    budgetRimasto = 20
    portieriAcquistati = []
    calciatoriRimasti = 2
    for i in range (3):
        trovato = False
        while not trovato:
            massimo, giocatore = cercaMassimo (portieri)
            if budgetRimasto - massimo >= calciatoriRimasti:
                trovato = True
                budgetRimasto = budgetRimasto - massimo
                calciatoriRimasti = calciatoriRimasti - 1
            else:
                portieri.remove (giocatore)

        portieriAcquistati.append (giocatore)
        portieri.remove (giocatore)

    budgetRimasto = 40
    difensoriAcquistati = []
    calciatoriRimasti = 7
    for i in range (8):
        trovato = False
        while not trovato:
            massimo, giocatore = cercaMassimo (difensori)
            if budgetRimasto - massimo >= calciatoriRimasti:
                trovato = True
                budgetRimasto = budgetRimasto - massimo
                calciatoriRimasti = calciatoriRimasti - 1
            else:
                difensori.remove (giocatore)

        difensoriAcquistati.append (giocatore)
        difensori.remove (giocatore)

    budgetRimasto = 80
    centrocampistiAcquistati = []
    calciatoriRimasti = 7
    for i in range (8):
        trovato = False
        while not trovato:
            massimo, giocatore = cercaMassimo (centrocampisti)
            if budgetRimasto - massimo >= calciatoriRimasti:
                trovato = True
                budgetRimasto = budgetRimasto - massimo
                calciatoriRimasti = calciatoriRimasti - 1
            else:
                centrocampisti.remove (giocatore)

        centrocampistiAcquistati.append (giocatore)
        centrocampisti.remove (giocatore)

    budgetRimasto = 120
    attaccantiAcquistati = []
    calciatoriRimasti = 5
    for i in range (6):
        trovato = False
        while not trovato:
            massimo, giocatore = cercaMassimo (attaccanti)
            if budgetRimasto - massimo >= calciatoriRimasti:
                trovato = True
                budgetRimasto = budgetRimasto - massimo
                calciatoriRimasti = calciatoriRimasti - 1
            else:
                attaccanti.remove (giocatore)

        attaccantiAcquistati.append (giocatore)
        attaccanti.remove (giocatore)

    stampa (portieriAcquistati, difensoriAcquistati, centrocampistiAcquistati, attaccantiAcquistati)

def stampa (portieriAcquistati, difensoriAcquistati, centrocampistiAcquistati, attaccantiAcquistati):
    print ("Portieri: ", end = " ")
    for i in range (len (portieriAcquistati)):
        print (f"{portieriAcquistati[i][0]} {portieriAcquistati[i][1]}", end = " ")

    print ()

    print ("Difensori: ", end = " ")
    for i in range (len (difensoriAcquistati)):
        print (f"{difensoriAcquistati[i][0]} {difensoriAcquistati[i][1]}", end = " ")

    print ()

    print ("Centrocampisti: ", end = " ")
    for i in range (len (centrocampistiAcquistati)):
        print (f"{centrocampistiAcquistati[i][0]} {centrocampistiAcquistati[i][1]}", end = " ")

    print ()

    print ("Attaccanti: ", end = " ")
    for i in range (len (attaccantiAcquistati)):
        print (f"{attaccantiAcquistati[i][0]} {attaccantiAcquistati[i][1]}", end = " ")

    print ()    

def cercaMassimo (lista):
    massimo = 0
    for i in range (len (lista)):
        if lista[i][1] > massimo:
            massimo = lista[i][1]
            giocatore = lista[i]

    return massimo, giocatore

def main ():
    portieri, difensori, centrocampisti, attaccanti = leggiFile ("fantacalcio.txt")
    gioco (portieri, difensori, centrocampisti, attaccanti)

main ()