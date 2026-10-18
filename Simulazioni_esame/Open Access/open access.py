import csv

def leggiFile (pubblicazioni, editori):
    dictEditori = {}
    infilePubblicazioni = open (pubblicazioni, "r")
    infileeditori = open (editori, "r")

    for line in infileeditori:
        #Wiley; 3000
        line = line.strip().split(";")
        line[1] = int (line[1])
        dictEditori [line[0]] = [line[1], 0, 0]

    for line in infilePubblicazioni:
        line = line.strip().split(";")
        editore = line[1]
        openAccess = line[2]
        if openAccess == "TRUE":
            dictEditori[editore][1] = dictEditori[editore][1] + 1

        dictEditori[editore][2] = dictEditori[editore][2] + 1

    infileeditori.close ()
    infilePubblicazioni.close ()
    return dictEditori
def stampa (editori):
    massimo = 0
    edMax = ""
    print (f"Pubblicazioni per editore:")

    #nomeEditore : [prezzo, open, totali]
    for editore in sorted (editori):
        prezzo = editori[editore][0]
        openSource = editori[editore][1]
        totale = editori[editore][2]
        try:
            percentuale = openSource * 100 / totale
        except ZeroDivisionError:
            percentuale = 0
        if percentuale == 0:
            print (f"{editore:<13s}: {totale:4d} articoli")
        else:
            print (f"{editore:<13s}: {totale:4d} articoli, {percentuale:6.2f}% open source")

        costo = openSource * prezzo
        if costo > massimo:
            massimo = costo
            edMax = editore

    print ()

    print (f"Editore con costo massimo: {edMax} ({massimo})")

def main ():
    try:
        editori = leggiFile ("PublicationData.csv", "publisher_fees.txt")
        stampa (editori)
    except FileNotFoundError:
        print ("File non trovato")
    except ValueError:
        print ("Hai cambiato il tipo a qualcosa che non può cambiare tipo")
    except KeyError:
        print ("Errore nella gestione del dizionario")

main ()