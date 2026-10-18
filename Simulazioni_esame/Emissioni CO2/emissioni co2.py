

def leggiFile (filename):
    infile = open (filename, "r")

    nome = filename

    primaRiga = infile.readline()
    primaRiga = primaRiga.split (";")
    
    grandezze = primaRiga [2:]

    paesi = dict ()

    minimo = 0
    massimo = 0 #tanto sono anni, per forza positivi

    for line in infile:
        #AUS;2013;399288;176363;137311;69870
        parti = line.split (";")
        codice = parti[0]
        anno = int(parti[1])

        if minimo == 0:
            minimo = anno

        valori = parti[2:]

        for i in range (len (valori)):
            valori[i] = int (valori[i])
        
        if codice not in paesi:
            anni = dict ()
            anni [anno] = valori
        else:
            anni[anno] = valori

        paesi[codice] = anni

        if anno > massimo:
            massimo = anno

        if anno < minimo:
            minimo = anno

    infile.close ()

    return minimo, massimo, paesi, grandezze, nome
def stampaAVideo (minimo, massimo, paesi, grandezze, nome):
    indice = -100
    infile = open ("queries.txt", "r")

    print ("nome del file", nome)
    print (f"Anni monitorati: da {minimo} a {massimo}")
    print ("Quantità monitorate:", end = " ")
    for i in range (len (grandezze)):
        print (grandezze[i], end = " ")
    
    print ()
    print()

    for line in infile:
        #paese AUS Gas
        parti = line.split ()
        tipo = parti[0]

        if tipo == "paese":
            codice = parti[1]
            parametro = parti[2]

            anni = paesi[codice]

            indice = decisioneIndice (parametro)

            valorePrimoAnno = anni[minimo][indice]
            valoreUltimoAnno = anni[massimo][indice]

            incremento = (valoreUltimoAnno * 100 / valorePrimoAnno) - 100
            
            print (f"Paese: {codice} - Valore: {parametro}")
            for anno in anni:
                print (f"{anno:7d}", end = " ")
            print ()

            for anno in anni:
                print (f"{anni[anno][indice]:7d}", end = " ")
            print ()
            print (f"Differenza: {incremento:.2f}%")

            print()

        elif tipo == "massimo":
            anni = paesi[codice]
            maxValore = 0
            minValore = 0
            anno = int(parti[1])
            parametro = parti[2]
            indice = decisioneIndice (parametro)
            print (f"Anno: {anno} - Valore: {parametro}")
            for paese in paesi:
                valore = paesi[paese][anno][indice]

                if minValore == 0:
                    minValore = valore

                if valore > maxValore:
                    maxValore = valore
                    sigla = paese
                
                if valore < minValore:
                    minValore = valore

            differenza = (maxValore * 100 / minValore) -100

            print (f"Paese massimo: {sigla} ({maxValore}, +{differenza:.2f}% rispetto al minimo)")

    infile.close ()

def decisioneIndice(parametro):
    indice = -1
    if parametro == "Totale":
        indice = 0
    elif parametro == "Carbone":
        indice = 1
    elif parametro == "Petrolio":
        indice = 2
    elif parametro == "Gas":
        indice = 3

    return indice

def main ():
    (minimo, massimo, paesi, grandezze, nome) = leggiFile ("GCB2023.csv")
    stampaAVideo(minimo, massimo, paesi, grandezze, nome)

main ()