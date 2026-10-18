import csv

def leggiFile (aeroporto, database):
    dictAutPass = dict ()
    dictAutisti = {}
    dictFermate = {}
    fileAero = open (aeroporto, "r")
    fileData = open (database, "r")

    csvReader = csv.reader (fileAero)
    primaRiga = next (csvReader)

    primaRiga = primaRiga[2:]

    IDFermate = dict ()
    listaFermate = list ()

    for i in range (len (primaRiga)):
        IDFermate[primaRiga[i]] = {"saliti": 0, "scesi": 0}
        listaFermate.append (primaRiga[i])

    for line in csvReader:
        codice = line[0]
        stops = line[2:]
        for i in range (len (stops)):
            if "/" in stops[i]:
                sal = int (stops[i].split("/")[0])
                sce = (int (stops[i].split("/")[1]))
            elif stops[i] == "--":
                sal = 0
                sce = 0
            elif int (stops[i]) > 0:
                sal = int (stops[i])
                sce = 0
            else:
                sal = 0
                sce = (int (stops[i]))

            passeggeri = IDFermate[listaFermate[i]]
            passeggeri["saliti"] = passeggeri["saliti"] + sal
            passeggeri["scesi"] = passeggeri["scesi"] + abs(sce)

            if codice not in dictAutPass:
                dictAutPass[codice] = 0

            dictAutPass[codice] = dictAutPass[codice] + sal

    for line in fileData:
        line = line.strip().split (": ")
        if line[0][0] == "A":
            dictAutisti [line[0]] = line[1]
        else:
            dictFermate[line[0]] = line[1]
        
    return dictAutisti, dictFermate, dictAutPass, IDFermate

def stampa (dictAutisti, dictFermate, dictAutPass, IDFermate):
    massimo = 0
    minimo = 0
    for fermata in IDFermate:
        salESce = IDFermate[fermata]
        if minimo == 0:
            minimo = salESce["scesi"]

        if salESce ["saliti"] > massimo:
            massimo = salESce["saliti"]
            nomeMax = dictFermate[fermata]

        if salESce["scesi"] > minimo:
            minimo = salESce["scesi"]
            nomeMin = dictFermate [fermata]

    print (f"La fermata in cui salgono più passeggeri ({massimo}) è {nomeMax}")

    print (f"La fermata in cui scendono più passeggeri ({minimo}) è {nomeMin}")

    dictAutPass = dict (sorted (dictAutPass.items (), key = lambda x:x [1], reverse = True))

    for IDAutista in dictAutPass:
        print (f"{dictAutisti[IDAutista]} con {dictAutPass[IDAutista]} passeggeri")

        

def main ():
    dictAutisti, dictFermate, dictAutPass, IDFermate = leggiFile ("dati_aeroporto_torino.csv", "database.txt")
    stampa (dictAutisti, dictFermate, dictAutPass, IDFermate)

main ()