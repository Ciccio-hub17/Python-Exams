import string

#funzione per aprire i file e creare le strtture dati
#param: i nomi dei due file
#return: due liste
def leggiFile (fileParole, fileMurphy):
    argomenti = open (fileParole, "r", encoding = "UTF-8")
    infileMurphy = open (fileMurphy, "r", encoding = "UTF-8")

    #inizializzo una lista in cui mettere le frasi e una stringa vuota
    leggi = []
    legge = ""
    #ciclo sul file delle frasi
    for line in infileMurphy:
        line = line.strip()
        line = line.strip(string.punctuation)
        #se la line è vuota, inizializza la mia stringa e appendi la legge alla lista
        if line != "":
            #se la mia stringa è vuota, allora metto semplicemente il titolo
            if legge == "":
                legge = legge + line
            #altrimenti metto un trattino
            else:
                legge = legge + " - " + line

        else:
            leggi.append (legge)
            legge = ""
    #mi splitto la legge in titolo e enunciato e li metto in una lista
    leggiGiuste = []
    for legge in leggi:
        legge = legge.split (" - ")
        leggiGiuste.append (legge)
    
    parole = []
    #salvo gli argomenti in una lista
    for line in argomenti:
        line = line.strip ()
        parole.append (line)

    infileMurphy.close ()
    argomenti.close ()

    return parole, leggiGiuste
#calcoli: è la funzione di stampa
#param: le du strtture dati create prima
#return: niente, perchè stampa
def calcolo (parole, leggi):
    #mi creo una lista di tuple al fine di creare un dizionario, per gestire se la frase è gia stata scritta oppure no
    leggiNuove = []
    for legge in leggi:
        titolo = legge[0]
        enunciato = legge[1]
        leggiNuove.append ((titolo, enunciato))
    
    leggiModificate = dict (leggiNuove)

    #ciclo sulle parole e poi sulle leggi
    for parola in parole:
        for legge in leggi:
            #risultato è un booleano
            risultato = confronto (parola, legge[1])
            if risultato:
                #sfrutto il fatto che modificando il dizionario, posso far sollevare un keyerror e non far stampare la frase
                try:
                    #controllo se i caratteri sono più di 50
                    if len (leggiModificate[legge[0]]) > 50:
                        #stampo il titolo
                        print (f"{legge[0]}", end = " - ")
                        #e l'enunciato
                        for i in range (50):
                            print (leggiModificate[legge[0]][i], end = "")
                        #e i puntini per dire che non è finito
                        print ("...")
                        #tolgo la frase stampata dal dizionario
                        leggiModificate.pop (legge[0])
                    #vuol dire che i caratteri sono meno di 50 e quindi posso stampare per intero
                    else:
                        print (f"{legge[0]}", end = " - ")
                        print (f"{leggiModificate[legge[0]]}.")
                except KeyError:
                    pass

#confronto: parola e legge (solo enunciato)
def confronto (parola, legge):
    #fondamentalmente creo una lista in cui c'è l'enunciato con le parole 'pulite'
    legge = legge.split ()
    for i in range (len (legge)):
        legge[i] = legge[i].strip (string.punctuation).lower ()
    #in questo modo posso vedere se la mia parola è nella lista e ritorno un booleano
    if parola in legge:
        return True
    else:
        return False
    
#funzione principale
def main ():
    parole, leggi = leggiFile ("argomenti.txt", "leggi_di_Murphy.txt")
    calcolo (parole, leggi)

main ()