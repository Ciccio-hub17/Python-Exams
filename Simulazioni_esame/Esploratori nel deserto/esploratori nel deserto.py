from csv import reader
from math import sqrt, trunc

def leggiFile (fileDeserto, fileEsploratori):
    deserto = open (fileDeserto, "r")
    esploratori = open (fileEsploratori, "r")

    desertReader = reader(deserto)
    rigaprima = next(desertReader)
    posizioniOasi = []
    dizionarioEsploratori = {}

    #salvo le posizioni delle sole oasi in una lista di tuple
    for line in desertReader:
        coordinate = (int(line[0]), int(line[1]))
        if line[2] == "oasis":
            posizioniOasi.append(coordinate)

    riga1 = esploratori.readline()
    #101,117,155,4.882601218952981,10
    
    #per gli esploratori faccio un dizionario con chiave : id ; valore: lista del tipo: coord.X, coord.y e massimo dei km percorribili (valore troncato)
    for line in esploratori:
        parti = line.strip().split(",")
        id = parti[0]
        coordinataX = int (parti[1])
        coordinataY = int (parti[2])
        maxKm = trunc(float (parti[3]) * int (parti[4]))
        dizionarioEsploratori[id] = [coordinataX, coordinataY, maxKm]

    deserto.close()
    esploratori.close()

    return dizionarioEsploratori, posizioniOasi

def uscitaDeserto (dizionarioEsploratori, posizioniOasi):
    salvi = []
    morti = []
    #ciclo ogni esploratore fino a quando esce o muore
    for esploratore in dizionarioEsploratori:
        oasiVisitate = set()
        morto = False
        uscito = False
        coordinataX = dizionarioEsploratori[esploratore][0]
        coordinataY = dizionarioEsploratori[esploratore][1]
        chilometriMassimi = dizionarioEsploratori[esploratore][2]
        risultato = controlloUscitaDeserto (coordinataX, coordinataY, chilometriMassimi, salvi, esploratore)
        if risultato == None:
            while True:
                distanzaMinima = 500
                for oasi in posizioniOasi:
                    coordinataOasiX = oasi[0]
                    coordinataOasiY = oasi[1]
                    distanza = round(sqrt((coordinataX - coordinataOasiX)** 2 + (coordinataY - coordinataOasiY)**2))
                    if distanza < distanzaMinima and oasi not in oasiVisitate:
                        distanzaMinima = distanza
                        coordinataOasiVicinaX = coordinataOasiX
                        coordinataOasiVicinaY = coordinataOasiY

                if distanzaMinima <= chilometriMassimi:
                    coordinataX = coordinataOasiVicinaX
                    coordinataY = coordinataOasiVicinaY
                    oasiVisitate.add((coordinataOasiVicinaX, coordinataOasiVicinaY))
                    risultato = controlloUscitaDeserto (coordinataX, coordinataY, chilometriMassimi, salvi, esploratore)
                    if risultato != None:
                        break

                else:
                    lista = []
                    lista.append (esploratore)
                    lista.append ((dizionarioEsploratori[esploratore][0], dizionarioEsploratori[esploratore][1]))
                    morti.append(lista)
                    break

    percentualeSalvi = (100 * len(salvi)) / len(dizionarioEsploratori)
    print ("Sopravvissuti: ", percentualeSalvi, "%")

    print ("Recupero Salme esploratori:")
    for element in morti:
        print (f"<{element[0]}>: {element[1]}")

def controlloUscitaDeserto (coordinataX, coordinataY, chilometriMassimi, salvi, esploratore):
    if 500 - coordinataX <= chilometriMassimi:
        salvi.append (esploratore)
        return salvi
    elif 500 - coordinataY <= chilometriMassimi:
        salvi.append(esploratore)
        return salvi
    elif coordinataX <= chilometriMassimi:
        salvi.append(esploratore)
        return salvi
    elif coordinataY <= chilometriMassimi:
        salvi.append(esploratore)
        return salvi
    else:
        return None

def main ():
    try:
        (dizionarioEsploratori, posizioniOasi) = leggiFile ("desert.csv", "survivors.txt")
        uscitaDeserto (dizionarioEsploratori, posizioniOasi)
    except FileNotFoundError:
        print ("Impossibile trovare il file")
    except ValueError:
        print ("Errore nella conversione dei dati")
    except KeyError:
        print ("Errore nella gestione del dizionario")
    except IndexError:
        print ("Errore nella gestione delle liste ")

main ()