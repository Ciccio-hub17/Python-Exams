from math import *
import csv

RAGGIO = 6731

def leggifile (bambini, province):
    infileBambini = open (bambini, "r")
    infileProvince = open (province, "r")
    dizionario = {}

    csvBambini = csv.reader (infileBambini)
    csvProvince = csv.reader (infileProvince)

    next(csvBambini)
    next(csvProvince)

    for line in csvBambini:
        #Potter,Harry,Bacchetta,VE
        nome = line[1] + " " + line[0]
        regalo = line[2]
        provincia = line[-1]
        if provincia not in dizionario:
            dizionario[provincia] = [nome, regalo]
        else:
            dizionario[provincia] = [dizionario[provincia]]
            dizionario[provincia].append ([nome, regalo])

    for line in csvProvince:
        #84,19,,Agrigento,AG,37.31109,13.576548
        sigla = line[4]
        lat = float(line[5]) * pi / 180
        long = float(line[6]) * pi / 180

        if sigla in dizionario:
            try:
                dizionario[sigla][0].append (lat)
                dizionario[sigla][0].append (long)
                dizionario[sigla][1].append (lat)
                dizionario[sigla][1].append (long)
            except:
                dizionario[sigla].append (lat)
                dizionario[sigla].append (long)

    infileBambini.close ()
    infileProvince.close ()

    return dizionario

def stampa (dizionario):
    #prendo il primo
    #'VE': ['Harry Potter', 'Bacchetta', 0.7940034743678213, 0.21672975052489984]

    lista = []
    for provincia in dizionario:
        if type(dizionario[provincia][0]) == list:
            lista.append ((provincia, dizionario[provincia][0]))
            lista.append ((provincia, dizionario[provincia][1]))
        else:
            lista.append ((provincia, dizionario[provincia]))

    lista = sorted (lista, key = lambda x:x [1][2], reverse=True)

    pro = lista[0][0]
    regalo = lista[0][1][1]
    nome = lista[0][1][0]
    latIniziale = lista[0][1][2]
    longIniziale = lista[0][1][3]


    print (f"Consegnato {regalo} a {nome} ({pro})")
    lista.pop (0)
    flag = True

    while len (lista) != 0:

        if flag:
            latitudine1 = latIniziale
            longitudine1 = longIniziale
            flag = False

        minimo = RAGGIO

        for i in range (len (lista)):
            latitudine2 = lista[i][1][2]
            longitudine2 = lista[i][1][3]
            distanza = calcola_distanza (latitudine1, longitudine1, latitudine2, longitudine2)
            if distanza < minimo:
                minimo = distanza
                pro = lista[i][0]
                regalo = lista[i][1][1]
                nome = lista[i][1][0]
                indice = i
                latIniziale = lista[i][1][2]
                longIniziale = lista[i][1][3]

        flag = True
        print (f"   Viaggio di {minimo} km")
        print (f"Consegnato {regalo} a {nome} ({pro})")
        lista.pop (indice)

def calcola_distanza (latitudine1, longitudine1, latitudine2, longitudine2):
    h = (sin ((latitudine1 - latitudine2)/2)**2 + cos (latitudine1) * cos (latitudine2) * sin ((longitudine1 - longitudine2)/2)**2)
    distanza = 2 * RAGGIO * asin (sqrt(h))

    return distanza

def main ():
    dizionario = leggifile ("bambini.csv", "province.csv")
    stampa (dizionario)
main ()