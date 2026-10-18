def creazioneTabella (filename):
    infile = open (filename, "r")

    griglia = []
    for i in range (6):
        lista = []
        for j in range (7):
            lista.append ("-")
        griglia.append (lista)

    print ("griglia vuota")

    for i in range (6):
        for j in range (7):
            print (griglia[i][j], end = "")
        print ()

    mosse = []
    for line in infile:
        parti = line.split ()
        parti[1] = int (parti[1])
        mosse.append (parti)

    print (mosse)


    infile.close ()
    return griglia, mosse


def gioco (griglia, mosse):
    vinto = False
    giocata = 0
    k = 0
    while not vinto:
        i = len (griglia) - 1
        giocatore = mosse[giocata][0]
        if giocatore == "G1":
            j = mosse[k][1]

            while griglia[i][j] != "-":
                i = i - 1
            
            griglia[i][j] = "X"
            print ("Gioca il giocatore 1")
            for m in range (6):
                for n in range (7):
                    print (griglia[m][n], end = "")
                print ()
            
        else:
            j = mosse[k][1]

            while griglia[i][j] != "-":
                i = i - 1
            
            griglia[i][j] = "O"
            print ("Gioca il giocatore 2")
            for m in range (6):
                for n in range (7):
                    print (griglia[m][n], end = "")
                print ()

        giocata = giocata + 1
        k = k + 1

        vinto = controllo (griglia, i, j, giocatore)
    
    return giocatore


def controllo (griglia, riga, posizionej, giocatore):
    if giocatore == "G1":
        vinto = False
        conta = 1
        i = 1
        try:
            while griglia[riga][posizionej - i] == "X":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga][posizionej + i] == "X":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej] == "X":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej + i] == "X":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej - i] == "X":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto  
        except IndexError:
            pass

    else:
        vinto = False
        conta = 1
        i = 1
        try:
            while griglia[riga][posizionej - i] == "O":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga][posizionej + i] == "O":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej] == "O":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej + i] == "O":
                conta = conta + 1
                i = i + 1

                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass
        conta = 1
        i = 1
        try:
            while griglia[riga + i][posizionej - i] == "O":
                conta = conta + 1
                i = i + 1
                if conta == 4:
                    vinto = True
                    return vinto
        except IndexError:
            pass

    return vinto            

def main ():
    try:
        (griglia, mosse) = creazioneTabella ("mosse.txt")
        giocatore = gioco (griglia, mosse)
        print (f"Ha vinto il giocatore {giocatore}")
    except FileNotFoundError:
        print ("File non trovato")

main ()