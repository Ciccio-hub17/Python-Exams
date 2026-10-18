def leggiFile (acquisti, prodotti):
    dictProdotti = {}
    rivenditori = set ()
    inAcquisti = open (acquisti, "r")
    inProdotti = open (prodotti, "r")

    for line in inProdotti:
        line = line.strip().split ()
        dictProdotti[line[0]] = [line[1]]

    for line in inAcquisti:
        line = line.strip().split ()
        if line[1] not in dictProdotti[line[0]]:
            dictProdotti[line[0]].append(line[1])

        rivenditori.add (line[1])

    inProdotti.close ()
    inAcquisti.close ()
    return dictProdotti, rivenditori

def controllo (dictProdotti, rivenditori):
    print ("Elenco transazioni sospette")
    for prodotto in dictProdotti:
        if len (dictProdotti[prodotto]) != 1:
            print (f"Codice prodotto: {prodotto}")
            print (f"Rivenditore ufficiale: {dictProdotti[prodotto][0]}")
            print (f"Lista rivenditori:", end = "")
            lista = dictProdotti[prodotto]
            for i in range (len (lista)):
                if lista[i] in rivenditori:
                    print (f"{lista[i]}", end = " ")

            print ()
            print ()

def main ():
    dictProdotti, rivenditori = leggiFile ("acquisti.txt", "prodotti.txt")
    controllo (dictProdotti, rivenditori)
main ()