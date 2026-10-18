NO_AUTO = "XXXXXXX"

def main ():
    try:
        print ("Ciao")
        filename = input ("File da leggere: ")
    except FileNotFoundError:
        print ("File name non trovato")
    gestisciIncrocio(filename)

def gestisciIncrocio (filename):
    infile = open (filename, "r")
    outfile = open ("precedenze.txt", "w")
    incrocio = [[], [], []]

    leggo = True
    numAuto = 0

    while leggo or numAuto != 0:
        if leggo:
            riga = infile.readline()
            if riga == "":
                leggo = False
            else:
                targhe = riga.split()
                for i in range (3):
                    if targhe[i] != NO_AUTO:
                        incrocio[i].append(targhe[i])
                        numAuto = numAuto + 1
        if numAuto != 0:
            massima = 0
            if len (incrocio[1]) > len (incrocio[massima]):
                massima = 1
            if len (incrocio[2]) > len (incrocio[massima]):
                massima = 2
            daScrivere = incrocio [massima].pop(0)
            numAuto = numAuto - 1
            outfile.write (f"{daScrivere} \n") 
        print(numAuto)
    
    print ("Controllare il file precedenze.txt")

    infile.close()
    outfile.close()

main()