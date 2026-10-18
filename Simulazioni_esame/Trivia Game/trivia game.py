from random import choice, shuffle
from operator import itemgetter

def leggiFile (filename):
    domande = dict ()
    infile = open (filename, "r", encoding = "UTF-8")

    linea = ""

    for line in infile:
        if line != "\n":
            line = line.strip()    
            linea = linea + "," + str(line)
        else:
            parti = linea.split (",")
            parti.pop(0)
            domanda = parti[0]
            difficolta = int(parti [1])
            rispostaCorretta = parti[2]
            risposteErrate = [parti[3], parti[4], parti[5]]
            interno = {"Risposta Corretta" : rispostaCorretta, "Risposte Errate": risposteErrate}
            lista = [domanda, interno]

            if difficolta not in domande:
                domande [difficolta] = [lista]
            else:
                domande [difficolta].append(lista)
            linea = ""

    infile.close ()
    return domande

def presentazione (domande):
    nickName = input ("Dammi il tuo nickname ")
    rispostaGiusta = False
    livello = 0
    punteggio = 0
    while not rispostaGiusta:
        try:
            domandaCorrente = choice (domande[livello])
            print (f"Livello {livello}) {domandaCorrente[0]}")

            lista, indice = disordina (domandaCorrente[1])

            print (f"       1.{lista[0]}")
            print (f"       2.{lista[1]}")
            print (f"       3.{lista[2]}")
            print (f"       4.{lista[3]}")
            ok1 = False
            while not ok1:
                try:
                    numero = int(input ("Inserisci la risposta: "))
                    if numero not in [1, 2, 3, 4]:
                        numero = int ("")
                    ok1 = True
                except ValueError:
                    print ("Riprova") 
            if numero == indice:
                punteggio = punteggio + 1
                print ("Risposta Corretta!")
                print ()
                livello = livello + 1
            else:
                rispostaGiusta = True
                print (f"Risposta sbagliata! La risposta corretta era {indice}")
                print ()
        except KeyError:
            print ("Hai raggiunto il punteggio massimo")
            break

    print (f"Hai totalizzato {punteggio} punti")

    punteggi (nickName, punteggio)

def punteggi (nickname, punteggio):
    infile = open ("punti.txt", "r")
    tabella = []
    for line in infile:
        lista = []
        parti = line.strip (). split ()
        nome = parti[0]
        punti = int (parti[1])
        lista.append (nome)
        lista.append (punti)
        tabella.append (lista)

    flag = False
    for i in range (len(tabella)):
        if nickname == tabella[i][0]:
            tabella[i][1] = tabella[i][1] + punteggio
            flag = True
    
    if flag == False:
        tabella.append ([nickname, punteggio])

    infile.close ()
    tabella = sorted (tabella, key = lambda x:x[1], reverse = True)

    scrivi (tabella)

def scrivi (tabella):
    infile = open ("punti.txt", "w")
    for i in range (len (tabella)):
        infile.write (f"{tabella[i][0]} {tabella[i][1]}\n")

    infile.close ()


def disordina (risposte):
    lista = []
    rispostaGiusta = risposte ["Risposta Corretta"]
    lista.append (rispostaGiusta)
    risposteSbagliate = risposte ["Risposte Errate"] 
    lista.append (risposteSbagliate[0])
    lista.append (risposteSbagliate[1])
    lista.append (risposteSbagliate[2])

    shuffle (lista)

    for i in range (len (lista)):
        if lista[i] == rispostaGiusta:
            indice = i + 1

    return lista, indice

def main ():
    domande = leggiFile ("domande.txt")
    presentazione (domande)

main ()