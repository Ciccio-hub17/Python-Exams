from math import sqrt

def leggifile (droni, stop):
    dictDroni = {}
    dictStop = {}
    infileDroni = open (droni, "r")
    infileStop = open (stop, "r")

    for line in infileDroni:
        line = line.strip().split (":")
        stazioni = line[1].split (",")
        dictDroni[line[0]] = stazioni

    for line in infileStop:
        line = line.strip().split (":")
        coordinate = line[1].split (",")
        dictStop [line[0]] = (int (coordinate[1]), int (coordinate[0]))

    infileDroni.close ()
    infileStop.close ()
    return dictStop, dictDroni

def calcoli (stop, droni):
    rapporto = {}
    for drone in droni:
        distanzaTotale = 0
        for i in range (len (droni[drone]) - 1):
            stazione1 = droni[drone][i]
            stazione2 = droni[drone][i+1]

            distanza = calcola_distanza (stazione1, stazione2, stop)
            distanzaTotale = distanzaTotale + distanza
            
            numeroDaMettere = distanzaTotale / len (droni[drone])
            rapporto [drone] = (numeroDaMettere, distanzaTotale)

    droneMax = sorted (rapporto.items (), key = lambda x:x[1][0], reverse = True)

    print (f"highest battery capacity for {droneMax[0][0]}")
    print (f"total distance = {droneMax[0][1][1]}")
    print (f"number of stops {len (droni[droneMax[0][0]]) - 1}")

def calcola_distanza (stazione1, stazione2, stop):
    coordinate1 = stop [stazione1]
    coordinate2 = stop [stazione2]

    distanza = sqrt ((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    return distanza

def main ():
    stop, droni = leggifile ("drones.txt", "stops.txt")
    calcoli (stop, droni)
main ()