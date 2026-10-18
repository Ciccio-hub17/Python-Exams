def leggiMorse (filename):
    codice = {}
    infile = open (filename, "r")
    for line in infile:
        parti = line.strip().split()
        lettera = parti[0]
        code = parti[1]
        codice [lettera] = code

    infile.close ()
    return codice

def codifica (filename, codice):
    infile = open (filename, "r")
    for line in infile:
        parti = line.strip().split ()
        codifica = parti[0]
        nomefile = parti[1]
        if codifica == "c":
            #Mettetevi in salvo!
            print (f"Codifica del file {nomefile}:")
            daTestoAMorse (codice, nomefile)
        else:
            print (f"Decodifica del file {nomefile}:")
            daMorseATesto (codice, nomefile)

    infile.close ()

def daTestoAMorse (codice, nomefile):
    infile = open (nomefile, "r")
    riga = infile.readline()

    for carattere in riga:
        carattere = carattere.upper ()
        try:
            print (f"{codice[carattere]}", end = " ")
        except KeyError:
            pass

    print ()
    infile.close ()

def daMorseATesto (codice, nomefile):
    codiceContrario = {}
    infile = open (nomefile, "r")
    tupla = list(codice.items ())
    for i in range (len (tupla)):
        codiceContrario [tupla[i][1]] = tupla[i][0]

    riga = infile.readline ()
    parti = riga.strip().split()
    for carattere in parti:
        try:
            print (f"{codiceContrario[carattere]}", end = "")
        except KeyError:
            pass

    infile.close ()

def main ():
    try:
        codice = leggiMorse ("morse.txt")
        codifica ("comandi.txt", codice)
    except FileNotFoundError:
        print ("File non trovato")

main ()