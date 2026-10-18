
def leggiFile (fiumi):
    infile = open (fiumi, "r")
    
    fiumi = dict ()
    for line in infile:
        line = line.rstrip()
        interno = dict ()
        fiumi [line] = interno

    infile.close ()
    return fiumi

def calcoloFiumi (dizionarioFiumi, filename):
    piogge = []


    #Enugu Aguobuumumba 07°19’N 07°13’E 900
    try:
        infile = open (filename, "r")
    except FileNotFoundError:
        pass
    nome = ""

    for i in range (len(filename)):
        if filename[i] != ".":
            nome = nome + filename[i]
        else:
            break

    
    if nome not in dizionarioFiumi:
        print (f"{nome.upper()} Informazioni non trovate")
        print ()
    else:
        print (f"{nome.upper()}", end = "    ")

        primaRiga = infile.readline ()
        
        secondaRiga = infile.readline ()

        secondaRiga = secondaRiga.strip().split()

        zona = secondaRiga[1]

        coordinate = f"({secondaRiga[2]}" + " " + f"{secondaRiga[3]})"

        daStampare = zona + " " + coordinate

        print (f"measured in {daStampare}")

        spazio = infile.readline()

        etichette = infile.readline ()
        #Humidity Pressure Windspeed Rainfall Radiation Tair Tearth-skin	Discharge

        etichette = etichette.strip().split ()

        sommaUmidita = 0
        massimoVento = 0
        massimaTemp = 0
        sommaTemp = 0
        conta = 0

        for line in infile:
            #64.75	986.73	0.37	1.72	18.85	24.03	23.35	12.01
            line = line.split ()
            for j in range (len (line)):
                line [j] = float (line[j])

            piogge.append (line[3])
            
            sommaUmidita = sommaUmidita + line[0]
            

            if line[2] > massimoVento:
                massimoVento = line[2]
            
            if line [6] > massimaTemp:
                massimaTemp = line [5]

            sommaTemp = sommaTemp + line [5]

            conta = conta + 1

        mediaUmidita = sommaUmidita / conta
        mediaTemp = sommaTemp / conta

        print (f"Avg. humidity {mediaUmidita:.2f}%")
        print (f"Max Wind speed: {massimoVento}m/s")
        print (f"Average Temperature: {mediaTemp:.2f}°C (max: {massimaTemp:.2f}°C)")
        print ()

    try:
        infile.close ()
        return piogge
    except UnboundLocalError:
        pass

def calcoloPiogge (piogge):
    mediaPiogge = []
    i = 0
    while i < 52:
        sommaPiogge = 0

        for j in range (len(piogge)):
            sommaPiogge = sommaPiogge + piogge[j][i]

        media = sommaPiogge / len (piogge)
        mediaPiogge.append (media)

        i = i + 1

    print ("Average weekly rain (MM):")
    conta = 0
    for i in range (len (mediaPiogge)):
        if conta != 6:
            print (f"{mediaPiogge[i]:.2f}", end = "   ")
            conta = conta + 1
        else:
            print (f"{mediaPiogge[i]:.2f}")
            conta = 0
    somma = 0
    for i in range (len (mediaPiogge)):
        somma = somma + mediaPiogge[i]

    mediaTotale = somma / len (mediaPiogge)
    print ()
    print (f"Yearly Average: {mediaTotale:.2f}mm")
    
def main ():
    piogge = []

    fileFiumi = ["ajali.dat", "adada.dat", "imo.dat", "ivo.dat", "otamiri.dat"]

    fiumi = leggiFile ("rivers.txt")

    for i in range (len (fileFiumi)):
        listaPiogge = calcoloFiumi (fiumi, fileFiumi[i])
        if listaPiogge != None:
            piogge.append (listaPiogge)

    calcoloPiogge (piogge)

main ()