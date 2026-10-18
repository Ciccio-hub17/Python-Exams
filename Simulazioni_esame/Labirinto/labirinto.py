from random import choice

def leggiFile(filename):
    infile = open (filename, "r")
    labirinto = []

    partenza = infile.readline()
    partenza = partenza.split (",")
    coordinatePartenza = [int(partenza[0]), int(partenza[1])]

    arrivo = infile.readline()
    arrivo = arrivo.split (",")
    coordinateArrivo = [int(arrivo[0]), int(arrivo[1])]

    for line in infile:
        line = line.rstrip()
        lista = []
        for i in range (len(line)):
            lista.append(line[i])

        labirinto.append (lista)

    infile.close()

    return (coordinatePartenza, coordinateArrivo, labirinto)

def raggiungimentoUscita(partenza, arrivo, labirinto):
    elenco_movimenti = [list (partenza)]
    posizione = list(partenza)
    movimento = 1
    while elenco_movimenti [-1] != arrivo:

        i = posizione [0]
        j = posizione[1]

        mosse_possibili = []

        if labirinto [i+1] [j] != "X" and labirinto [i+1] [j] != "V":
            mosse_possibili.append ([i+1, j])
        if labirinto [i] [j+1] != "X" and labirinto [i] [j+1] != "V":
            mosse_possibili.append ([i, j+1])
        if labirinto [i-1] [j] != "X" and labirinto [i-1] [j] != "V":
            mosse_possibili.append ([i-1, j])
        if labirinto [i] [j-1] != "X" and labirinto [i] [j-1] != "V":
            mosse_possibili.append ([i, j-1])

        
        if labirinto[i][j] == [14, 8] or labirinto[i][j] == [13, 9]:
            exit

        if len(mosse_possibili) != 0:
            elenco_movimenti.append (posizione)
            mossa = choice (mosse_possibili)
            posizione = list(mossa)
            print (f"movimento {movimento}: {mossa}")
            movimento = movimento + 1
        elif  len(mosse_possibili) == 0 and elenco_movimenti [-1] != arrivo:
            posizione = elenco_movimenti.pop(-1)
            print (f"movimento {movimento}: {posizione}")
            movimento = movimento + 1

        labirinto [i][j] = "V"

        
    
def main ():
    ok = False
    while not ok:
        try:
            (partenza, arrivo, labirinto) = leggiFile("labirinto.txt")
            raggiungimentoUscita (partenza, arrivo, labirinto)
            ok = True
        except FileNotFoundError:
            print ("Impossibile trovare il file")
        except ValueError:
            print ("Errore nella conversione dei dati da stringa a intero")
        except IndexError:
            pass

main ()