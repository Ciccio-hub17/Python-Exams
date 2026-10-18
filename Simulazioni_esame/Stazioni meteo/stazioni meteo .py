import statistics

TORINO = "Torino.csv"
#Data e Ora;Temp;Rugiada;Pressione;Umidita'
#01-01-17 00:00;4.6;2.1;1028;84

def main ():
    filename = input ("File da leggere: ")
    (dizionario, etichette) = leggiFile(filename)
    stampaVideo(dizionario, etichette)

def leggiFile (filename):
    infile = open (filename, "r")

    dizionario = {}

    line = infile.readline()
    etichette = line.strip().split (";")
    etichette.pop(0)
    for line in infile:
        parti = line.split(";")
        dataOra = parti[0].split()
        data = dataOra[0]
        parti.pop(0)
        
        if data not in dizionario:
            giornata = {}
            for i in range (len (etichette)):
                giornata[etichette[i]] = [float(parti[i])]
            dizionario [data] = giornata
        else:
            giornata = dizionario[data]
            for i in range (len(etichette)):
                giornata[etichette[i]].append(float(parti[i]))

    infile.close()
    return (dizionario, etichette)


def stampaVideo (dizionario, etichette):
    tabellaPerStampare = []
    print (" " * 12, end = "")
    for etichetta in etichette:
        print (f"{etichetta}", end = "   ")
    print ()
    for data in dizionario:
        tabellaPerStampare = []
        print (data)
        giornata = dizionario [data]
        for etichetta in giornata:
            lista = giornata [etichetta]
            statistiche = calcolaStatistiche (lista)
            tabellaPerStampare.append(statistiche)
        for j in range (len (tabellaPerStampare[0])):
            if j == 0:
                print ("   Media", end = " ")
            if j == 1:
                print (" Massimo", end = " ")
            if j == 2:
                print ("  Minimo", end = " ")
            if j == 3:
                print ("    Moda", end = " ")
            
            for i in range (len(tabellaPerStampare)):
                print (f"{tabellaPerStampare[i][j]:^10.2f}", end = "")
            print ()

        


            

def calcolaStatistiche (lista):
    media = float(sum (lista) / len(lista))
    massimo = float(max (lista))
    minimo = float(min (lista))
    moda = float(statistics.mode (lista))

    return (media, massimo, minimo, moda)



main ()