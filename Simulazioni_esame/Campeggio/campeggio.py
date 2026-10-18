OCCUPAZIONE = "occupazione.txt"
PREZZI = "prezzi.txt"
CALENDARIO = "calendario.txt"

def lettura (filename):
    infile = open(filename, "r")
    table = []
    for line in infile:
        parts = line.split(";")
        table.append(parts)

    table.pop(0)



    infile.close

    return table

def calcoli(occupazione, prezzi, calendario):
    #1;01/06/23;09/06/23;tenda;2;0;sì
    #01/06/23;07/06/23;8.00;15.00;2.00;1.00;
    dateArrivo = []
    datePartenza = []
    for i in range (len(occupazione)):
        dateArrivo.append(occupazione[i][1]) 
        datePartenza.append(occupazione[i][2])

    print (dateArrivo)

    print (datePartenza)

    giornoArrivo = []
    giornoPartenza = []
    meseArrivo = []
    mesePartenza = []
    for i in range (len(dateArrivo)):

        dataArrivoSplit = dateArrivo[i].split ("/")
        giornoArrivo.append(dataArrivoSplit[0])
        meseArrivo.append(dataArrivoSplit[1])
        dataPartenzaSplit = datePartenza[i].split ("/")
        giornoPartenza.append(dataPartenzaSplit[0])
        mesePartenza.append(dataPartenzaSplit[1])

    print (giornoArrivo)
    print (giornoPartenza)
    print (meseArrivo)
    print (mesePartenza)



    


def main ():
    inoccupazione = lettura (OCCUPAZIONE)
    inprezzi = lettura (PREZZI)
    incalendario = lettura (CALENDARIO)
    for i in range (len (inoccupazione)):
        calcoli (inoccupazione, inprezzi, incalendario)






main()