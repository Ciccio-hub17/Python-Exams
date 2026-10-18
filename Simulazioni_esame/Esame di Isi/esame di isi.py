from random import *

def leggiFile (filename, partita, difficolta, partiteVinte, partitePerse):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    listaAlfabeto = []
    for ch in alfabeto:
        listaAlfabeto.append (ch)

    infile = open (filename, "r")

    parole = []

    for line in infile:
        line.strip()
        parole.append (line)

    parolaScelta = choice (parole)

    punti = 10

    partiteVinte, partitePerse = gioco (parolaScelta, partita, listaAlfabeto, punti, difficolta, partiteVinte, partitePerse)

    infile.close ()

    return partiteVinte, partitePerse

def gioco (parola, partita, listaAlfabeto, punti, difficolta, partiteVinte, partitePerse):

    print (f"Partita n {partita}")
    print (f"IL bot ha scelto la difficoltà {difficolta}")

    lettera = ""
    conta = len(parola)
    while punti != 0 and conta != 0:

        print (f"Punti {punti} - La parola da indovinare è", end = ":")

        for i in range (len (parola)):
            if lettera == parola[i]:
                print (lettera, end = " ")
            else:
                print ("_", end =" ")

        print ()

        lettera = choice (listaAlfabeto)
        print (f"Lettera scelta dal bot: {lettera}")

        listaAlfabeto.remove (lettera)

        if lettera not in parola:
            print (f"Lettera {lettera} non è presente")
            punti = punti - 1
        else:
            print (f"Lettera {lettera} è presente:", end = "")
            for i in range (len (parola)):
                if lettera == parola[i]:
                    print (lettera, end = " ")
                else:
                    print ("_", end = " ")
            print ()

            conta = conta - 1

        print ()

    if punti == 0:
        print (f"Peccato, il bot ha perso. La parola da indovinare era {parola}")
        partitePerse = partitePerse + 1
    else:
        print (f"Complimenti, il bot ha indovinato correttamente la parola {parola}")
        partiteVinte = partiteVinte + 1

    return partiteVinte, partitePerse

def main ():
    print ("Ciao, gioco akinator")
    partita = 0
    flag = True
    partiteVinte = 0
    partitePerse = 0
    while flag:
        partita = partita + 1
        listaFile = ["facile.txt", "medio.txt", "difficile.txt"]
        file = choice (listaFile)

        if file == "facile.txt":
            difficolta = "facile"
        elif file == "difficile.txt":
            difficolta = "difficile"
        else:
            difficolta = "medio"

        partiteVinte, partitePerse = leggiFile (file, partita, difficolta, partiteVinte, partitePerse)
        ok = False
        while not ok:
            giocoSN = input ("Vuoi giocare ancora (S/N)? ")
            print ()
            if giocoSN != "S" and giocoSN != "N":
                print ("Input non valido, riprova")
                print ()
            else:
                ok = True
        if giocoSN == "N":
            flag = False

    print ("SESSIONE TERMINATA")
    print (f"IL bot ha vinto {partiteVinte} partita/e")
    print (f"Il bot ha perso {partitePerse} partite")

main ()