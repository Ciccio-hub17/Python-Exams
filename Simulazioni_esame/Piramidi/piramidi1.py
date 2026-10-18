def leggiFile (filename):
    infile = open (filename, "r")
    mappa = []

    for line in infile:
        line = line.strip().split ()
        for i in range (len (line)):
            line[i] = int (line[i])
        mappa.append (line)

    infile.close ()
    return mappa

def controllo_cime (mappa):
    direzioni = crea_direzioni ()
    for i in range (len (mappa)):
        for j in range (len (mappa[0])):
            massimo = controllo_massimo (direzioni, i, j, mappa)
            if massimo:
                print (f"{mappa[i][j]}", end = " ")
            else:
                print ("-", end = " ")
        print ()

def controllo_massimo (direzioni, riga, colonna, mappa):
    for d in direzioni:
        try:
            if mappa[riga][colonna] <= mappa[riga + d[0]][colonna + d[1]]:
                return False
        except IndexError:
            continue
        
    return True

def crea_direzioni ():
    direzioni = []
    for i in range (-1, 2):
        for j in range (-1, 2):
            direzioni.append ((i, j))

    direzioni.remove ((0,0))

    return direzioni



def main ():
    mappa = leggiFile ("mappa.txt")
    controllo_cime (mappa)

main ()