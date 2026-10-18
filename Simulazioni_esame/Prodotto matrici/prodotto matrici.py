def leggiMatrice (filename):
    matrici = []
    dimensioni = []
    infile = open (filename, "r")
    for line in infile:
        matrice = []
        line = line.strip().split ()
        for i in range (len (line)):
            line[i] = int (line[i])

        riga = line [0]
        colonna = line[1]
        contatore = 2
        dimensioni.append ((riga, colonna))
        for l in range (riga):
            lista = []
            for c in range (colonna):
                lista.append (line[contatore])
                contatore = contatore + 1
            matrice.append (lista)
        
        matrici.append (matrice)
    infile.close ()
    return matrici, dimensioni

def prodotto (matrici, dimensioni):
    if controllo_matrici_adiacenti (dimensioni):
        print (f"Matrici da moltiplicare: ", end = "")
        for i in range (len (dimensioni)):
            print (f"{dimensioni[i][0]} x {dimensioni[i][1]}", end = ", ")
        print ()
        tuplaMinimo = calcolo_numero_operazioni (dimensioni)
        print (f"Moltiplicazione delle matrici con dimensioni ({tuplaMinimo[1]}, {tuplaMinimo[2]}) e ({tuplaMinimo[2]}, {tuplaMinimo[3]}) -> ({tuplaMinimo[1]}, {tuplaMinimo[3]})")
        dimensioni.remove ((tuplaMinimo[1], tuplaMinimo[2]))
        dimensioni.remove ((tuplaMinimo[2]), tuplaMinimo[3])
        matrice1, matrice2 = identificaMatriciDaMoltiplicare (matrici, tuplaMinimo[1], tuplaMinimo[2], tuplaMinimo[3])
        matriceProdotto = calcola_prodotto (matrice1, matrice2)

        
    else:
        print ("Impossibile eseguire il prodotto, le matrici non sono adiacenti")

def identificaMatriciDaMoltiplicare (matrici, riga, colonna, colonnaSecondaMatrice):
    for i in range (len (matrici) - 1):
        if len (matrici[i]) == riga and len (matrici[i][0]) == colonna:
            matrice1 = matrici[i]
            matrice2 = matrici [i+1]
            break

    return matrice1, matrice2


def calcola_prodotto (matrice1, matrice2):
    matriceProdotto = []
    for i in range (len (matrice1)):
        lista = []
        for j in range (len (matrice2[0])):
            elemento = 0
            for k in range (len (matrice2)):
                elemento = elemento + matrice1[i][k] * matrice2[k][j]
            lista.append (elemento)
        matriceProdotto.append (lista)

    return matriceProdotto

def calcolo_numero_operazioni (dimensioni):
    numeroOp = []
    for i in range (len (dimensioni) - 1):
        numero = dimensioni[i][0] * dimensioni [i][1] * dimensioni [i+1][1]
        numeroOp.append ((numero, dimensioni[i][0], dimensioni [i][1], dimensioni [i+1][1]))

    minimo = numeroOp[0][0]
    tuplaMinimo = ()
    for i in range (1, len (numeroOp)):
        if numeroOp [i][0] < minimo:
            minimo = numeroOp [i][0]
            tuplaMinimo = numeroOp[i]

    return tuplaMinimo

def controllo_matrici_adiacenti (dimensioni):
    for i in range (len (dimensioni) - 1):
        if dimensioni[i][1] != dimensioni[i + 1][0]:
            return False
        
    return True

def main ():
    try:
        matrici, dimensioni = leggiMatrice ("matrices.txt")
        prodotto (matrici, dimensioni)
    except FileNotFoundError:
        print ("File not found")

main ()