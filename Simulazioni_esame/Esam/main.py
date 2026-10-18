#leggiFile:
#param: nome del file
#return: niente
def leggiFile (filename):
    infile = open (filename, "r")


    #permette di calcolare tutte le direzioni possibili 
    direzioni = calcola_direzioni ()

    #metto il contenuto del file in una tabella
    mappa = []

    #metto le cornici di 0
    lista = []
    for i in range (8):
        lista.append (0)

    mappa.append (lista)

    #carico la tabella mettendo uno 0 prima e dopo la riga
    for line in infile:
        lista = []
        line = line.strip()
        lista.append (0)
        for i in range (len (line)):
            lista.append (int (line[i]))

        lista.append (0)

        mappa.append (lista)

    #metto l'ultima riga di 0
    lista = []
    for i in range (8):
        lista.append (0)

    mappa.append (lista)

    #inizializzo una lista che in posizione 0 ha una tupla e in posizione 1 il valore della vista
    #cosi da semplificare l'output
    vista = []

    #ciclo sulla mappa utilizzando la funzione per calcolare la vista e la appendo alla lista
    for i in range (1, len(mappa)-1):
        for j in range (1, len (mappa[0])-1):
            vistaTotale = calcola_vista (mappa, i, j, direzioni)
            vista.append ([(i-1, j-1), vistaTotale])

    #ordino la lista in base al valore di vista
    vista = sorted (vista, key = lambda x:x [1], reverse = True)

    #stampo quanto richiesto
    for i in range (len (vista)):
        print (f"{i+1} {vista[i][0]} : Valore = {vista[i][1]}")

    infile.close ()
#calcola_vista: calcola la vista totale dall'altezza di un edificio
#param: la mappa, la riga e la colonna in cui ci troviamo e la lista delle direzioni percorribili
#return: la vista totale da quell'edificio
def calcola_vista (mappa, riga, colonna, direzioni):
    #inizializzo vista totale
    vistaTotale = 0
    #ciclo per ogni direzione possibile
    for d in direzioni:
        #controllo se non vado fuori dalla tabella
        try:
            #capisco quanto vale la vista parziale e la aggiungo alla vista totale
            vistaParziale = mappa[riga][colonna] - mappa[riga + d[0]][colonna + d[1]]
            vistaTotale = vistaTotale + vistaParziale
        #se si va fuori dalla tabella non è un problema, quindi continua il ciclo
        except IndexError:
            continue

    return vistaTotale

#calcola tutte le direzioni possibili mettendole in una lista di tuple
#param: nulla
#return: la lista di tuple con tutte le direzioni
def calcola_direzioni ():

    direzioni = []
    #prendo tutte le direzioni possibili di raggio 1 
    for i in range (-1, 2):
        for j in range (-1, 2):
            direzioni.append ((i, j))

    #rimuove la direzione 0, 0 per non fare un controllo con se stessa
    direzioni.remove ((0, 0))

    #ritorno la lista
    return direzioni

#funzione principale
def main ():
    #controllo se il file è presente e se non ci sono errori nelle conversioni
    try:
        leggiFile ("mappa.txt")
    except FileNotFoundError:
        print ("File nontrovato")
    except ValueError:
        print ("Errore nelle conversioni")
main ()