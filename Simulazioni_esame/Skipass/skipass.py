def  leggiTempi (filename):
    infile = open (filename, "r")
    tempi = {}
    for line in infile:
        parti = line.split()
        id = int(parti[0])
        orario = parti[1].split (":")
        tempo = int(orario[0]) * 60 + int(orario[1])
        tempi [id] = tempo

    infile.close()
    print (tempi)

    return tempi

def leggiPassaggi (tempi):
    filename = input ("Dammi il nome del file ")
    data = input ("Dammi la data ")
    infile = open (filename, "r")

    passaggi = 0
    sciatori = {}
    anomalie = []

    for line in infile:
        parti = line.split ()
        if parti [1] == data.strip():
            passaggi = passaggi + 1
            if parti[0] not in sciatori:
                sciatori[parti[0]] = orarioInSecondi(parti[2]) + tempi [int(parti[3])]

            else:
                orario = orarioInSecondi(parti[2])
                if orario < sciatori[parti[0]]:
                    anomalie.append (parti)

                sciatori[parti[0]] = orario + tempi [int(parti[3])]

    if len (anomalie) == 0:
        print ("nessuna anomalia")
    else:
        print ("Anomalie")
        for anomalia in anomalie:
            print (f"\tSkipass id: {anomalia[0]} - Impianto {anomalia[3]} - Ora: {anomalia[2]}")


    print (f"Numero medio di passaggi: {passaggi / len(sciatori):.2f}")
    infile.close()

def orarioInSecondi (stringa):
    parti = stringa.split(":")
    return int (parti[2]) + int (parti[1]) * 60 + int (parti[0]) * 3600

def main ():
    try:
        tempi = leggiTempi("tempi.dat")
        leggiPassaggi (tempi)
    except FileNotFoundError:
        print ("File non trovato")

main ()