import string

def leggiFile (favola, personaggi):
    dictPersonaggi = {}
    infileFavola = open (favola, "r")
    infilePersonaggi = open (personaggi, "r")

    

    for line in infilePersonaggi:
        line = line.strip()
        dictPersonaggi [line] = 0

    for line in infileFavola:
        line = line.strip().split ()
        for i in range (len (line)):
            line[i] = line[i].strip(string.punctuation).upper ()

            if line[i] in dictPersonaggi:
                dictPersonaggi[line[i]] = dictPersonaggi[line[i]] + 1

    infileFavola.close ()
    infilePersonaggi.close ()
    return dictPersonaggi

def stampaVideo (dictPersonaggi):
    personaggiNonPresenti = set ()
    for personaggio in dictPersonaggi:
        if dictPersonaggi[personaggio] == 0:
            personaggiNonPresenti.add (personaggio)

    persMax, persMin, personaggi = ricercaMassimoMinimo (dictPersonaggi)

    for i in range (len (personaggi)):
        if personaggi[i][1] != 0:
            print (f"{personaggi[i][0]}: {personaggi[i][1]} occorrenze")

    print (f"Il personaggio più ricorrente è {persMax}, quello meno ricorrente è {persMin}")
    scriviFile (personaggiNonPresenti)

def scriviFile (personaggi):
    infile = open ("personaggi_altri.txt", "w")

    for element in personaggi:
        infile.write (f"{element}\n")

    infile.close ()

def ricercaMassimoMinimo (dictPersonaggi):
    personaggi = sorted(dictPersonaggi.items (), key = lambda x:x[0])
    massimo = personaggi[0][1]
    minimo = personaggi[0][1]
    persMax = 0
    persMin = 0
    for i in range (1, len (personaggi)):
        if personaggi [i][1] != 0:
            if personaggi [i][1] > massimo:
                massimo = personaggi [i][1]
                persMax = personaggi[i][0]

            if minimo == 0:
                minimo = personaggi [i][1]
            
            if personaggi [i][1] < minimo:
                minimo = personaggi [i][1]
                persMin = personaggi [i][0]

    return persMax, persMin, personaggi

def main ():
    dictPersonaggi = leggiFile ("favola.txt", "personaggi.txt")
    stampaVideo (dictPersonaggi)

main ()