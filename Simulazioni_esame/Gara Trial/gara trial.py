def leggiFile (partecipanti, penalita):
    dizionario = {}
    infilePartecipanti = open (partecipanti, "r")
    infilePenalita = open (penalita, "r")

    for line in infilePartecipanti:
        line = line.strip().split (":")
        dizionario[line[0]] = [line[1]]

    for line in infilePenalita:
        line = line.strip().split (":")
        penalita = line[1:]
        
        for i in range (len (penalita)):
            penalita[i] = int (penalita[i])

        somma = sum (penalita)

        contaMassima = 0
        conta = 0
        for i in range (0, len (penalita) - 1, 2):
            if penalita[i] == 0:
                conta = conta + 1
                if penalita[i + 1] == 0:
                    conta = conta + 1
                else:
                    contaMassima = conta
                    conta = 0
            else:
                conta = 0

            if conta > contaMassima:
                contaMassima = conta
        
        contaMassima = contaMassima + 1
        print (contaMassima)
        for i in range (len (penalita)):
            dizionario[line[0]].append (penalita[i])

        dizionario[line[0]].append (somma)
        dizionario[line[0]].append (contaMassima)

    infilePartecipanti.close ()
    infilePenalita. close ()

    return dizionario

def calcoloVincitore (dizionario):
    classifica = sorted (dizionario.items (), key = lambda x:x [1][-2])
    print ("Classifica:")
    for i in range (len (classifica)):
        print (f"{classifica[i][1][0]:18s} {classifica[i][1][-2]} penalità")

    dizionario = dict (classifica)
    lista = sorted (dizionario.items (), key = lambda x:x [1][-1], reverse = True)

    nome = lista [0][1][0]
    conta = lista [0][1][-1]


    print (f"Ha realizzato la più lunga sequenza {nome} con {conta} prove consecutive superate")

def main ():
    dizionario = leggiFile ("partecipanti.txt", "penalita.txt")
    calcoloVincitore (dizionario)


main ()