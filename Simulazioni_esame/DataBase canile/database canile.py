import csv

def leggiFile (filename):
    razze = dict ()

    infile = open (filename, "r")
    csvReader = csv.reader(infile)

    next (csvReader)

    for lista in csvReader:     
        #6866-7072,Luna,German Shepherd,Intermediate,58.0
        razza = lista[2]
        livello = lista[3]
        punteggio = float(lista[-1])
        if razza not in razze:
            livelli = {"Beginner": [0, 0], "Intermediate": [0, 0], "Advanced": [0, 0], "Expert": [0, 0]}
            razze [razza] = livelli
            razze[razza][livello] = [punteggio, 1]
        else:
            num = razze[razza][livello][1]
            punteggioPrecedente = razze[razza][livello][0]
            punteggioNuovo = punteggioPrecedente + punteggio
            numeroNuovo = num + 1
            razze[razza][livello] = [punteggioNuovo, numeroNuovo]

    print (razze)
    
    infile.close()
    return razze

def calcoli (razze):
    expert = dict ()
    for razza in razze:
        print (f"Razza: {razza}")
        for livello in razze[razza]:
            if razze[razza][livello][1] != 0:
                media = razze[razza][livello][0] / razze[razza][livello][1]
                print(f"    Livello {livello}: {media:.2f}")

                if livello == "Expert":
                    expert [razza] = media

        print ()

    massimo = 0
    maxRazza = ""
    for razza in expert:
        if expert [razza] > massimo:
            massimo = expert [razza]
            maxRazza = razza

    print (f"La razza con il punteggio medio più alto è {maxRazza}")

def main ():
    try:
        razze = leggiFile ("dogs.csv")
        calcoli (razze)
    except FileNotFoundError:
        print ("File non trovato")

main ()