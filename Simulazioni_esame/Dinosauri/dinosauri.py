ROSSO = 5
VERDE = 3
GIALLO = 1

def leggifile (filename):
    lista = []
    giocatore1 = []
    giocatore2 = []
    infile = open (filename, "r")

    for line in infile:
        line = line.strip ()
        lista.append (line)

    for i in range (len (lista)):
        if (i%2) == 0:
            giocatore1.append (lista[i])
        else:
            giocatore2.append (lista[i])

    gioco (giocatore1, giocatore2)

    infile.close ()

def gioco (giocatore1, giocatore2):
    punteggio1 = 0
    punteggio2 = 0
    piattoTotale = 0

    print (f"Punteggio giocatore 1: {punteggio1}")

    print (f"Punteggio giocatore 2: {punteggio2}")

    for i in range (len (giocatore1)):
        print (f"Mano n {i + 1}")
        print (f"Carta Giocatore 1: {giocatore1[i]}")
        print (f"Carta Giocatore 2: {giocatore2[i]}")

        punteggioNuovo1, punteggioNuovo2, piatto = calcoloPunteggio (giocatore1[i], giocatore2[i])
        print (punteggioNuovo1, punteggioNuovo2)
        if piatto == 0:
            punteggio1 = punteggio1 + punteggioNuovo1
            punteggio2 = punteggio2 + punteggioNuovo2
            
            if punteggioNuovo1 > punteggioNuovo2:
                punteggio1 = punteggio1 + piattoTotale
                print (f"Risultato: Vince la mano il giocatore 1")
            else:
                punteggio2 = punteggio2 + piattoTotale
                print (f"Risultato: Vince la mano il giocatore 2")    
                
            piattoTotale = 0

        else:
            piattoTotale = piattoTotale + piatto
            print ("Risultato: Pareggio")

        print (f"Punteggio giocatore 1: {punteggio1}")

        print (f"Punteggio giocatore 2: {punteggio2}")

    if punteggio1 > punteggio2:
        print (f"Vince il giocatore 1 con {punteggio1} punti")
    else:
        print (f"Vince il giocatore 2 con {punteggio2} punti")

def calcoloPunteggio (carta1, carta2):

    piatto = 0
    punteggio1 = 0
    punteggio2 = 0
    if carta1 == "Rosso" and carta2 == "Verde":
        punteggio1 = ROSSO + VERDE
        punteggio2 = 0
    elif carta1 == "Rosso" and carta2 == "Giallo":
        punteggio1 = ROSSO + GIALLO
        punteggio2 = 0
    elif carta1 == "Verde" and carta2 == "Giallo":
        punteggio1 = VERDE + GIALLO
        punteggio2 = 0
    elif carta1 == "Verde" and carta2 == "Rosso":
        punteggio2 = ROSSO + VERDE
        punteggio1 = 0
    elif carta1 == "Giallo" and carta2 == "Rosso":
        punteggio2 = ROSSO + GIALLO
        punteggio1 = 0
    elif carta1 == "Giallo" and carta2 == "Verde":
        punteggio2 = VERDE + GIALLO
        punteggio1 = 0
    elif carta1 == "Rosso" and carta2 == "Rosso":
        punteggio1 = 0
        punteggio2 = 0
        piatto = 10
    elif carta1 == "Verde" and carta2 == "Verde":
        punteggio1 = 0
        punteggio2 = 0
        piatto = 6
    elif carta1 == "Giallo" and carta2 == "Giallo":
        punteggio1 = 0
        punteggio2 = 0
        piatto = 2
    
    return punteggio1, punteggio2, piatto

def main ():
    leggifile ("mazzo.txt")

main ()