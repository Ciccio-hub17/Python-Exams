FILE1 = "tetraminoes.txt"
FILE2 = "tetraminoes2.txt"

def leggiFile (filename):
    mossa = 1
    punti = 0
    infile = open (filename, "r")

    tabella = crea_tabella ()

    flag = True
    while flag:
        matrice = []
        for i in range (5):

            line = infile.readline()

            if i == 0:

                line = line.split (",")
                try:
                    x = int (line[0])
                    y = int (line[1])
                except ValueError:
                    flag=False

            else:

                lista = []
                lunghezza = len (line.strip())

                for i in range (lunghezza):
                    lista.append (int(line[i]))

                matrice.append (lista)
        if len (matrice[0]) != 0:
            ancoraDentro, tabella = inserimento (x, y, matrice, tabella)
        else:
            break

        print (f"Mossa {mossa}, punteggio {punti}")

        for i in range (6):
            print ("|", end = "")
            for j in range (8):
                if tabella[i][j] == 0:
                    print (f" ", end = "")
                else:
                    print (f"x", end = "")
            print ("|")

        print ("----------")
        print ()

        if ancoraDentro:
            vittoria, indice = controllo (tabella)
            mossa = mossa + 1
            if vittoria:
                punti = punti + 10
                tabella.pop (indice)
                lista = []
                for k in range (8):
                    lista.append (0)
                
                tabella.insert (0, lista)
        else:
            return False
        
    infile.close ()
    return True

def controllo (tabella):  
    for i in range (len(tabella)):
        conta = 0
        for j in range (len (tabella[0])):
            if tabella[i][j] == 1:
                conta = conta + 1

        if conta == 8:
            indice = i
            return True, indice
    indice = 0    
    return False, indice

def inserimento (riga, colonna, tetramino, tabella):
    riga = len (tabella)-1 - riga
    z = 0
    for i in range (riga,riga-4, -1):
        k = 0
        for j in range (colonna, colonna + 4):
            if  tetramino[len (tetramino) - 1 -z][k] == 1:
                if i >= 0:
                    tabella[i][j] = 1
                else:
                    return False, tabella
            else:
                try:
                    if tabella[i][j] != 1:
                        tabella[i][j] = 0
                except IndexError:
                    continue
            k = k + 1
        z = z + 1
    return True, tabella

def crea_tabella ():

    tabella = []
    for i in range (6):
        lista = []
        for j in range (8):
            lista.append (0)

        tabella.append (lista)

    return tabella

def main ():
    risultato = leggiFile (FILE1)
    if risultato:
        print ("Hai vinto")
    else:
        print ("Mi dispiace hai perso")

main ()