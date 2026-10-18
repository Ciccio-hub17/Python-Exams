import copy
D = 3

def leggiFile (filename):
    mappa = []
    infile = open (filename, "r")

    for line in infile:
        riga = line.strip().split()
        for i in range (len (riga)):
            riga [i] = int (riga[i])
        
        mappa.append (riga)
        
    infile.close ()
    return mappa

def massimo_locale(mappa, r, c, direzioni):
    for d in direzioni:
        try:
            if mappa[r][c] <= mappa[r + d[0]][c + d[1]]:
                return False
        except IndexError:
            continue
   
    return True

def creazione_hot_spot (mappa):
    copiaMappa = copy.deepcopy (mappa)
    direzioni = creazione_direzioni()
    for i in range (len(mappa)):
        for j in range (len (mappa[0])):
            if not massimo_locale (mappa, i, j, direzioni):
                copiaMappa [i][j] = "-"

    stampaMappa (copiaMappa)


def creazione_direzioni ():
    direzioni = []
    for i in range (-D, D + 1):
        for j in range (-D, D + 1):
            tupla = (i, j)
            direzioni.append (tupla)

    direzioni.remove ((0, 0))

    return direzioni
            
def stampaMappa (copiaMappa):
    for i in range (len(copiaMappa)):
        for j in range (len (copiaMappa[0])):
            print (copiaMappa[i][j], end = "  ")
        
        print ()

def main ():
    mappa = leggiFile ("mappa.txt")
    creazione_hot_spot(mappa)


main ()