from operator import itemgetter

def leggiNumeri(filename):
    infile = open(filename, "r")
    line = infile.read()
    numeriVincenti = line.split()
    infile.close()
    return numeriVincenti

def leggiPremi(filename):
    infile = open(filename, "r")
    vincite = dict()
    for line in infile:
        parts = line.split()
        vincite[int(parts[0])] = int(parts[1])
    infile.close()
    return vincite

def leggiSchedine(filename):
    infile = open(filename, "r")
    schedine = dict()
    costoSchedine = []
    for line in infile:
        parts = line.split(",")
        schedine[parts[0]] = parts[1:len(parts) - 1]   ### ___ !! la chiave del dizionario è STR e non INT !! ___
        costoSchedine.append(float(parts[-1]))
    infile.close()
    return schedine, costoSchedine

def visualizzazione(numeriVincenti, premi, schedine, costoSchedine):
    # ID_SCHEDINA: 1 NUMERI_INDOVINATI: 11 63 22 28 VINCITA: 30  TIPO PREMIO: 4
    totale = 0
    lista_temp=list()  ### ___ Necessaria per ordinamento ___
    print("SCHEDINE VINCENTI")
    for key in schedine:
        i = 0
        numeriVincentiPerSchedina = []
        vincitaPerSchedina = 0
        while i < len(numeriVincenti):
            if schedine[key][i] in numeriVincenti or schedine[key][i] == "*":
                numeriVincentiPerSchedina.append(schedine[key][i])
            i = i + 1
        for chiave in premi:
            if len(numeriVincentiPerSchedina) == chiave and len(numeriVincentiPerSchedina) > 2: ### ___ aggiunta la parte finale della condizione ___
                vincitaPerSchedina = chiave
                totale = totale + premi[vincitaPerSchedina]
                break


        if vincitaPerSchedina != 0:
            lista_temp.append((key, numeriVincentiPerSchedina, vincitaPerSchedina))

    ### for i in range(len(lista_temp)): ___ x controllo che tutto fosse ok ___
        ### print(lista_temp[i][0], lista_temp[i][1], lista_temp[i][2])

    lista_temp = sorted(lista_temp, key=itemgetter(1))  ### ___ ordinamento per numero di elementi in numeriVincentiPerSchedina ___

    for i in range(len(lista_temp)):   ### ___ visualizzazione corretta ___
        print(f"ID_SCHEDINA: {lista_temp[i][0]}  --  NUMERI_VINCENTI: ", end="")
        for j in range(len(lista_temp[i][1])):
            print(lista_temp[i][1][j], end=" ")
        print(f"VINCITA: {premi[lista_temp[i][2]]} PREMIO: {lista_temp[i][2]}")

    guadagnoLordo = sum(costoSchedine)
    guadagnoNetto = guadagnoLordo - totale
    print()
    print(f"Guadagno degli organizzatori: {guadagnoNetto}")


def main():
    numeriVincenti = leggiNumeri("vincente.txt")
    premi = leggiPremi("premi.txt")
    tupla = leggiSchedine("schedine.txt")
    schedine = tupla[0]
    costoSchedine = tupla[1]
    visualizzazione(numeriVincenti, premi, schedine, costoSchedine)

main()
