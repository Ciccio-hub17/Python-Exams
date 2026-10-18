def leggiFile (popolazione, green):
    dizionario = {}
    infilePopolazione = open (popolazione, "r")
    infileGreen = open (green, "r")

    for line in infilePopolazione:
        line = line.strip().split (";")
        line[1] = int (line[1])
        dizionario[line[0]] = [line[1]]

    for line in infileGreen:
        line = line.strip().split (";")
        line[1] = int (line[1])
        line[2] = int (line [2])
        dizionario[line[0]].append (line[1])
        dizionario[line[0]].append (line[2])

    infileGreen. close ()
    infilePopolazione.close ()

    return dizionario

def calcoli (dizionario):
    green = {}
    for nazione in dizionario:
        lista = dizionario[nazione]

        densitaAnimali = lista[1] / lista[0]
        densitaPiante = lista[2] / lista[0]

        indice = (densitaAnimali + densitaPiante) / 2 * 100

        green [nazione] = [densitaAnimali, densitaPiante, indice]
    stampa (green)

def stampa (green):
    green = dict (green)
    maxDensAn = sorted (green.items (), key = lambda x:x[1][0], reverse = True)
    maxDensAn = (maxDensAn[0][0], maxDensAn[0][1][0])
    
    green = dict (green)
    maxDensPi = sorted (green.items (), key = lambda x:x[1][1], reverse = True)
    maxDensPi = (maxDensPi[0][0], maxDensPi[0][1][1])

    green = dict (green)
    indice = sorted (green.items(), key = lambda x:x[1][2], reverse = True)

    print (f"La nazione con il più alto di animali per popolazione è {maxDensAn[0]} con un rapporto di {maxDensAn[1]:.4f}")

    print (f"La nazione con il più alto di piante per popolazione è {maxDensPi[0]} con un rapporto di {maxDensPi[1]:.4f}")

    print ("Le prime tre nazioni in ordine decrescente di Indice Green sono:")
    for i in range (3):
        print (f"{i+1}. {indice[i][0]} - Indice Green: {indice[i][1][2]:.2f}")

def main ():
    dizionario = leggiFile ("population.txt", "animal_plant_count.txt")
    calcoli (dizionario)

main ()