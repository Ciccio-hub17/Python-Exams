def leggiFile (filename):
    brani = []
    infile = open (filename, "r")

    for line in infile:
        lista = []
        parti = line.strip().split (":")
        nome = parti[0]
        note = parti[1].split ()
        lista.append (nome)

        for i in range (len(note)):
            lista.append (note[i])
        brani.append (lista)

    infile.close
    return brani

def controlloStampa (brani):
    for i in range (len (brani)):
        nome = brani[i][0]   
        flagPlagio, plagio = controlloPlagio (brani, i)
        flagCopiatura, copiatura = controlloCopiatura (brani, i)
        flagSospetto, sospetto = controlloSospetto (brani, i)

        if flagPlagio:
            print (f"{nome} è un PLAGIO di {plagio}")
        if flagCopiatura:
            print (f"{nome} è una COPIATURA di {copiatura}")
        if flagSospetto:
            print (f"{nome} è un SOSPETTO di {sospetto}")

        
def controlloPlagio (brani, i):
    flag = False
    note = brani[i][1:]
    for j in range (i):
        if brani[j][1:] == note:
            flag = True
            nome = brani[j][0]
            return flag, nome

    return flag, None

def controlloCopiatura (brani, i):
    flag = False
    note = brani[i][1:]
    tabella = []
    for n in range (len (note) - 5):
        lista = note[n: n+5]
        tabella.append (lista)
    for j in range (i):
        for k in range (len (brani[j][1:]) - 5):
            daVerificare = brani[j][k: k+5]
            if daVerificare in tabella:
                flag = True
                nome = brani[j][0]
                return flag, nome

    return flag, None

def controlloSospetto (brani, i):
    conta = 0
    flag = False
    tabella = []
    note = brani[i][1:]
    for n in range (len (note) - 5):
        lista = note[n: n+5]
        tabella.append (lista)
    for j in range (i):
        for k in range (1, len (brani[j][1:]) - 5):
            daVerificare = brani[j][k: k + 5]
            for n in range (len (tabella)):
                differenza = abs(int(daVerificare[0]) - int(tabella[n][0]))
                for m in range (len (tabella[n])):
                    if int(tabella[n][m]) - int(daVerificare[0]) == differenza:
                        conta = conta + 1
                if conta == 4:
                    return not flag, brani[0][0]
    return flag, None


def main():
    brani = leggiFile ("brani.txt")
    controlloStampa (brani)

main ()