def leggiFile (posizioni, risposte):
    dictRisposte = dict ()
    infilePosizioni = open (posizioni, "r")
    infileRisposte = open (risposte, "r")

    for line in infileRisposte:
        line = line.strip().split ()
        dictRisposte[line[0]] = line[1:]

    listaPosizioni = []
    for line in infilePosizioni:
        line = line.strip().split()
        listaPosizioni.append (line)

    infilePosizioni.close ()
    infileRisposte.close ()

    return listaPosizioni, dictRisposte

def stampa (listaPosizioni, dictRisposte):
    for i in range (len (listaPosizioni)):
        for j in range (len (listaPosizioni[i])):
            alunno = listaPosizioni[i][j]
            try:
                if j != 0:
                    alunnoPrima = listaPosizioni[i][j-1]
                    risultato = controllo (alunno, alunnoPrima, dictRisposte)
                    if risultato != "":
                        print (risultato)
            except IndexError:
                pass

            try:
                if j != len (listaPosizioni[i]) - 1:
                    alunnoDopo = listaPosizioni[i][j+1]
                    risultato = controllo (alunno, alunnoDopo, dictRisposte)
                    if risultato != "":
                        print (risultato)
            except IndexError:
                pass
    
def controllo (alunno1, alunno2, dictRisposte):
    risultato = ""
    if dictRisposte[alunno1] == dictRisposte[alunno2]:
        risultato = f"le risposte di {alunno1} sono uguali a quelle di {alunno2}"
        return risultato
    else:
        lista1 = []
        lista2 = []
        risposte1 = dictRisposte[alunno1]
        risposte2 = dictRisposte[alunno2]
        conta1 = 0
        conta2 = 0
        for i in range (len(risposte1)):
            if risposte1[i] != "-" and risposte2[i] != "-":
                lista1.append (risposte1[i])
                lista2.append (risposte2[i])
            elif risposte2[i] == "-" and risposte1[i] != "-":
                conta2 = conta2 + 1
                lista2.append (risposte1[i])
                lista1.append (risposte1[i])
            

        if lista1 == lista2 and conta2 >= 1:
            risultato = f"{alunno2} può aver copiato da {alunno1}"
            return risultato
        else:
            risposte1 = dictRisposte[alunno1]
            risposte2 = dictRisposte[alunno2]

            if risposte1 != risposte2:
                return ""
            
    return risultato

def main ():

    try:
        listaPosizioni, dictRisposte = leggiFile ("posizioni.txt", "risposte.txt")
        stampa (listaPosizioni, dictRisposte)
    except FileNotFoundError:
        print ("File non trovato")

main ()