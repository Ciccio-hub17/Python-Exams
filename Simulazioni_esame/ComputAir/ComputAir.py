
def creazioneDizionario(aereifile, tempofile):
    aerei = open (aereifile, "r")
    tempo = open (tempofile, "r")

    dictAerei = dict()
    dictTempo = dict()
    dictPasseggeri = dict()

    insiemeCitta = set()
    numeroPasseggeri = []


    for line in tempo:
        line = line.strip()
        parts = line.split(";")
        dictTempo [parts[0]] = parts[1]
        insiemeCitta.add(parts[0])

    for line in aerei:
        line = line.strip()

        parts = line.split(";")

        numeroPasseggeri.append(int(parts[2]))
        if parts[1] not in dictPasseggeri:
            dictPasseggeri[parts[1]] = int(parts[2])
        else:
            dictPasseggeri[parts[1]] = dictPasseggeri[parts[1]] + int (parts[2])
        dictAerei[parts[0]] = parts[1]

    print (dictAerei)
    print (dictTempo)

    numeroVoli = len(dictAerei)

    calcoli (dictAerei, dictTempo, insiemeCitta, numeroVoli, numeroPasseggeri, dictPasseggeri)

    aerei.close()
    tempo.close()

def calcoli(dictAerei, dictTempo, insiemeCitta, numerovoli, numeroPasseggeri, dictPasseggeri):
    numerovoli = int(numerovoli)
    print ("Numero medio di passeggeri:", end = " ")
    media = sum(numeroPasseggeri) / numerovoli
    print (media)

    print ("Visualizzazione dei voli con destinazione città con meteo stormy o rainy")
    for key in dictAerei:
        if dictTempo[dictAerei[key]] == "Stormy" or dictTempo[dictAerei[key]] == "Rainy":
            print (f"{key} verso {dictAerei[key]}: {dictTempo[dictAerei[key]]}")

    print ("Condizione delle città che sono destinazione di almeno un volo")
    print (insiemeCitta)

    for key in dictPasseggeri:
        if dictPasseggeri[key] != 0:
            print (f"{key}: {dictTempo[key]}. {dictPasseggeri[key]} passeggeri in arrivo")

def main ():
    creazioneDizionario ("flights.txt", "weather.txt")

main ()