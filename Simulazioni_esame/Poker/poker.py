from random import shuffle
from math import trunc

CARTE = ["7", "8", "9", "10", "J", "Q", "K", "A"]
SEMI = ["C", "F", "P", "Q"]

def genera_mazzo ():

    tabella = []
    for numero in CARTE:
        for seme in SEMI:
            lista = []
            lista.append (numero)
            lista.append (seme)
            tabella.append (lista)

    shuffle (tabella)

    return tabella

def crea_file (tabella):
    infile = open ("mazzo.txt", "w")
    for i in range (len (tabella)):
        infile.write (f"{tabella[i][0]} {tabella[i][1]}\n")

    infile.close ()

def controllo (tabella):
    infile = open ("mazzo.txt", "r")
    massimo = trunc (len (tabella)/ 5)

    for j in range (massimo):
        i = 0
        mano = []
        while i < 5:
            riga = infile.readline ()
            riga = riga.strip().split ()
            cartaSeme = (riga[0], riga[1])
            mano.append (cartaSeme)

            i = i + 1
        for k in range (len (mano)):
            print (f"{mano[k][0]}{mano[k][1]}", end = " ")
        print (" ", end = " ")
        risultatoReale = scalaReale (mano)
        if risultatoReale:
            print ("Scala Reale")
        else:
            risultatoPoker = poker (mano)
            if risultatoPoker:
                print ("Poker")
            else:
                risultatoColore = colore (mano)
                if risultatoColore:
                    print ("Colore")
                else:
                    risultatoFull = full(mano)
                    if risultatoFull:
                        print ("Full")
                    else:
                        risultatoScala = scala (mano)
                        if risultatoScala:
                            print ("Scala")
                        else:
                            risultatoTris = tris (mano)
                            if risultatoTris:
                                print ("Tris")
                            else:
                                risultatoDoppiaCoppia = doppia_coppia (mano)
                                if risultatoDoppiaCoppia :
                                    print ("Doppia Coppia")
                                else:
                                    risultatoCoppia = coppia (mano)
                                    if risultatoCoppia:
                                        print ("Coppia")
                                    else:
                                        print ("Niente")

    infile.close ()

def scalaReale (mano):
    numeriReali = [10, 11, 12, 13, 14]
    flag = False
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    associazioneValoreCarta = {}
    associato = 7
    for valore in CARTE:
        associazioneValoreCarta [valore] = associato
        associato = associato + 1

    listaDiControllo = []
    for carta in lista:
        listaDiControllo.append (associazioneValoreCarta[carta])

    listaDiControllo = sorted (listaDiControllo)
    if listaDiControllo == numeriReali:
        lista1 = []
        for i in range (len (mano)):
            lista1.append (mano[i][1])

        dizionarioSeme = {}
        for i in range (len (lista1)):
            if lista1[i] not in dizionarioSeme:
                dizionarioSeme[lista1[i]] = 1
            else:
                dizionarioSeme[lista1[i]] = dizionarioSeme[lista1[i]] + 1

        if len (dizionarioSeme) == 1:
            flag = True
        
    return flag

def poker (mano):
    flag = False
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    controllo = {}
    for i in range (len (lista)):
        if lista[i] not in controllo:
            controllo[lista[i]] = 1
        else:
            controllo [lista[i]] = controllo [lista[i]] + 1

    if len (controllo) == 2:
        for carta in controllo:
            if controllo [carta] == 4:
                flag = True
    
    return flag

def colore (mano):
    
    flag = False
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][1])

    controlloSemi = {}
    for i in range (len (lista)):
        controlloSemi[lista[i]] = 1

    if len(controlloSemi) == 1:
        flag = True
    
    return flag

def scala (mano):
    flag = False
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    associazioneValoreCarta = {}
    associato = 7
    for valore in CARTE:
        associazioneValoreCarta [valore] = associato
        associato = associato + 1

    listaDiControllo = []
    for carta in lista:
        listaDiControllo.append (associazioneValoreCarta[carta])

    listaDiControllo = sorted (listaDiControllo, reverse = True)

    conta = 0

    for i in range (len (listaDiControllo) - 1):
        if listaDiControllo[i] - listaDiControllo[i+1] == 1:
            conta = conta + 1

    if conta == 4:
        flag = True
    
    return flag


def coppia (mano):
    flag = False
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    controllo = set ()
    for i in range (len (lista)):
        if lista[i] not in controllo:
            controllo.add (lista[i])
        else:
            flag = True
            break

    return flag

def tris (mano):
    flag = False
    controllo = dict ()
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    for i in range (len (lista)):
        if lista[i] not in controllo:
            controllo[lista[i]] = 1
        else:
            controllo[lista[i]] = controllo[lista[i]] + 1

    for carta in controllo:
        if controllo[carta] == 3:
            flag = True
            break
    
    return flag

def doppia_coppia (mano):
    flag = False
    conta = 0
    controllo = dict ()
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    for i in range (len (lista)):
        if lista[i] not in controllo:
            controllo[lista[i]] = 1
        else:
            controllo[lista[i]] = controllo[lista[i]] + 1

    for carta in controllo:
        if controllo[carta] == 2:
            conta = conta + 1
        
        if conta == 2:
            flag = True
            break
    
    return flag

def full (mano):
    flag = False
    controllo = dict ()
    lista = []
    for i in range (len (mano)):
        lista.append (mano[i][0])

    for i in range (len (lista)):
        if lista[i] not in controllo:
            controllo[lista[i]] = 1
        else:
            controllo[lista[i]] = controllo[lista[i]] + 1

    if len (controllo) == 2:
        i = 1
        for carta in controllo:
            if i == 1:
                if controllo [carta] == 2 or controllo[carta] == 3:
                    if controllo[carta] == 2:
                        altraCarta = 3
                    else:
                        altraCarta = 2
            else:
                if controllo[carta] == altraCarta:
                    flag = True

            i = i + 1
        
        return flag

def main ():
    
    tabella = genera_mazzo ()
    crea_file (tabella)
    controllo (tabella)

main ()