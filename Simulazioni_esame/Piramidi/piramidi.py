#leggiFile:
#param: nome del file
#return mappa

def leggiFile (filename):
    mappa =[]
    infile = open (filename, "r")       #creo una tabella con
                                        #tutti i valori all'interno del file
    for line in infile:
        line = line.strip().split ()
        for i in range (len (line)):
            line[i] = int (line[i])
        mappa.append (line)

    infile.close ()
    return mappa

#controllocime:
#controlla se ogni elemento della tabella è una cima
#param: mappa 
#return: niente
def controlloCime (mappa):
    cime = []
    direzioni = creazione_direzioni ()                              #creo una lista con tutte le direzioni
    for i in range (len (mappa)):
        for j in range (len (mappa[0])):
            massimo = controlla_massimo (mappa, i, j, direzioni)    #ciclo per ogni elemento e vedo se è massimo
            if massimo:
                cime.append ((mappa[i][j], i, j))                   #se lo è lo appendo alla lista delle cime

    stampaVideo (cime)

#stampaVideo
#param: cime, che è una tupla del tipo (valore della cima, riga, colonna)
#return: niente
def stampaVideo (cime):
    somma = 0
    for i in range (len (cime)):
        somma = somma + cime [i][0]
        print (f"{cime[i][0]} {cime[i][1]} {cime[i][2]}")

    print ()

    media = somma / len (cime)

    print (f"Altezza media: {media:.2f}m")

#controlla_massimo
#param: mappa, riga e colonna dell'elemento, direzioni
#return: ritorna se l'elemento ricercato è un massimo oppure no
def controlla_massimo (mappa, r, c, direzioni):
    for d in direzioni:
        try:                                                #ciclo per tutte le direzioni, appena
            if mappa[r][c] <= mappa[r + d[0]][c + d[1]]:    #c'è un elemento che lo supera, torno False
                return False
        except IndexError:
            continue
    
    return True                                             #torno True proprio se è massimo

#creazione_direzioni:
#param: Nessuno
#return: tutte le direzioni possibili per un elemento della mappa

def creazione_direzioni ():
    direzioni = []
    for i in range (-1, 2):         #so che devo controllare gli elementi adiacenti in tutte le direzioni
        for j in range (-1, 2):     #quindi mi creo tutte le possibili combinazioni attraverso una lista di tuple
            tupla = (i, j)
            direzioni.append (tupla)

    direzioni.remove ((0, 0))       #tolgo l'elemento 0,0 per evitare di fare un confronto inutile
    
    return direzioni

def main ():
    try:
        mappa = leggiFile ("mappa.txt")     #creo una funzione per leggere la mappa (nome file come parametro)
        controlloCime (mappa)               #controllo le cime
    except ValueError:
        print ("Errore nella gestione delle conversione ad intero")
    except FileNotFoundError:
        print ("File non trovato")

main ()