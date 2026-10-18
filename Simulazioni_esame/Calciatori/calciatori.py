from operator import itemgetter

def main ():
    calciatori = leggiFile("statistiche.dat")
    interroga (calciatori)

def interroga (dizionarioRuolo):
    richiesta = input ("Che cosa vuoi fare? ")
    while richiesta.upper() == "C" or richiesta.upper() == "R":
        if richiesta.upper () == "R":
            ruolo = input ("Dammi il ruolo (A, C, D, P)")
            if ruolo.upper() in dizionarioRuolo:
                calciatori = dizionarioRuolo[ruolo]
                ordinati = sorted (calciatori.items(), key = itemgetter (1), reverse = True)
                print ("ECCO I GIOCATORI MIGLIORI")
                numero = min(3, len(calciatori))
                for i in range (numero):
                    calciatore = ordinati[i]
                    print (f"{calciatore[0]} {calciatore[1]}")
        
        elif richiesta.upper() == "C":
            calciatore1 = input ("Nome e cognome del primo calciatore: ").strip
            calciatore2 = input ("Nome e cognome del calciatore 2: ").strip
            ruolo1 = ""
            ruolo2 = ""
            punteggio1 = 0
            punteggio2 = 0
            for ruolo in dizionarioRuolo:
                calciatori = dizionarioRuolo[ruolo]
                if calciatore1 in calciatori:
                    ruolo1 = ruolo
                    punteggio1 = calciatori[calciatore1]
                    

                if calciatore2 in calciatori:
                    ruolo2 = ruolo
                    punteggio2 = calciatori[calciatore2]

            if ruolo1 =="" or ruolo2 == "":
                print ("qualcosa non va")
            elif ruolo1 == ruolo2:
                if punteggio2 > punteggio1:
                    print (f"Il migliore  è {calciatore2}")
                else:
                    print (f"Il migliore  è {calciatore1}")
            else:
                print("calciatori non confrontabili")

        richiesta = input ("Che cosa vuoi fare? ")

def calcolaPrestazione (lista):

    valore = float(lista[1]*0.5 + int(lista[2]) * 0.5 - int (lista[3]) * 0.2 - int(lista[4]) * 0.4) 
    return float(lista[0]) * valore

def leggiFile(filename):
    infile = open (filename, "r")
    dizionarioRuoli = dict() #chiave: ruolo
                             # valore : dizionario dei punteggi

    for line in infile:
        parts = line.split()
        nome = parts[0] + " " + parts[1]
        ruolo = parts[2]
        prestazione = calcolaPrestazione (line[3:])

        if ruolo not in dizionarioRuoli:
            calciatori = dict()
            calciatori[nome] = prestazione
            dizionarioRuoli[ruolo] = calciatori
        else:
            calciatori = dizionarioRuoli[ruolo]
            calciatori[nome] = prestazione

    infile.close()

main ()