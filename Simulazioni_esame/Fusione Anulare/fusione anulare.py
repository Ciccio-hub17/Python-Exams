#15 40 36
#10 A, 3 B e 7 C
from  math import trunc

def leggiFile (filename):
    infile = open (filename, "r")

    riga = infile.readline()

    risorse = riga.split ()

    for i in range (len (risorse)):
        risorse[i] = int (risorse[i])


    infile.close ()

    return risorse

def simulazione (risorse):
    energia = 0
    i = 0
    #primo ciclo di fusione nucleare
    moltiplicatoreNucleare, flag1 = ricerca_limitante_nucleare(risorse[0:3])
    risorse[0] = risorse[0] - moltiplicatoreNucleare * 10
    risorse[1] = risorse[1] - moltiplicatoreNucleare * 3
    risorse[2] = risorse[2] - moltiplicatoreNucleare * 7
    risorsaD = moltiplicatoreNucleare * 10
    risorsaE = moltiplicatoreNucleare * 15
    energiaNucleare = moltiplicatoreNucleare

    risorse.append (risorsaD)
    risorse.append (risorsaE)

    #primo ciclo di fusione anulare
    moltiplicatoreAnulare, flag2 = ricerca_limitante_anulare (risorse[3:])
    risorse[3] = risorse[3] - moltiplicatoreAnulare * 6
    risorse[4] = risorse[4] - moltiplicatoreAnulare * 5
    risorse[0] = risorse[0] + moltiplicatoreAnulare * 5
    risorse[1] = risorse[1] + moltiplicatoreAnulare * 7
    risorse[2] = risorse[2] + moltiplicatoreAnulare * 11
    energiaAnulare = moltiplicatoreAnulare * 2
    energia = energiaNucleare + energiaAnulare

    energiaTotale = energia 

    conta = 1

    cicloMax = 1
    energiaPrecedente = energia

    while i < 999 and (not flag1 or not flag2):
        moltiplicatoreNucleare, flag1 = ricerca_limitante_nucleare(risorse[0:3])
        risorse[0] = risorse[0] - moltiplicatoreNucleare * 10
        risorse[1] = risorse[1] - moltiplicatoreNucleare * 3
        risorse[2] = risorse[2] - moltiplicatoreNucleare * 7
        risorse[3] = risorse[3] + moltiplicatoreNucleare * 10
        risorse[4] = risorse[4] + moltiplicatoreNucleare * 15
        energiaNucleare = moltiplicatoreNucleare

        moltiplicatoreAnulare, flag2 = ricerca_limitante_anulare (risorse[3:])
        risorse[3] = risorse[3] - moltiplicatoreAnulare * 6
        risorse[4] = risorse[4] - moltiplicatoreAnulare * 5
        risorse[0] = risorse[0] + moltiplicatoreAnulare * 5
        risorse[1] = risorse[1] + moltiplicatoreAnulare * 7
        risorse[2] = risorse[2] + moltiplicatoreAnulare * 11
        energiaAnulare = moltiplicatoreAnulare * 2

        energia = energiaNucleare + energiaAnulare
        if energia >= energiaPrecedente:
            cicloMax = conta

        energiaTotale = energiaTotale + energia
        energiaPrecedente = energia

        conta = conta + 1

        i = i + 1

    print (f"energia totale {energiaTotale}MW")
    print (f"ciclo anulare più produttivo: {cicloMax}")

def ricerca_limitante_nucleare (risorse):

    flag = False
    multiploA = trunc (risorse[0] / 10)
    multiploB = trunc (risorse[1] / 3)
    multiploC = trunc (risorse[2] / 7)

    minimo = (min (multiploA, multiploB, multiploC))

    if minimo == 0:
        flag = True

    return minimo, flag

def ricerca_limitante_anulare (risorse):
    flag = False
    multiploD = trunc (risorse[0] / 6)
    multiploE = trunc (risorse[1] / 5)

    minimo = (min (multiploD, multiploD))

    if minimo == 0:
        flag = True

    return minimo, flag

def main ():
    risorse = leggiFile ("risorse.txt")
    simulazione (risorse)

main ()