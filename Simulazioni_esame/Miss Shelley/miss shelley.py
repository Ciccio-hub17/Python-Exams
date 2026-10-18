from math import trunc

def leggiCarrello (filename):
    carrello = {}
    infile = open (filename, "r")

    for line in infile:
        line = line.strip ()
        if line not in carrello:
            carrello[line] = 1
        else:
            carrello[line] = carrello[line] + 1

    infile.close ()
    return carrello

def leggiPrezzi (filename):
    prezzi = {}
    infile = open (filename, "r")

    for line in infile:
        line = line.strip().split(": ")
        prezzi [line[0]] = float(line[1])

    infile.close ()
    return prezzi

def leggiOfferte (filename):
    offerte = {}
    infile = open (filename, "r")

    for line in infile:
        parti = line.strip().split (": ")
        nomi = parti[0].split ()

        numero = len (nomi)
        regalo = parti[1]
        try:
            if nomi[0] != nomi[1]:
                offerte [parti[0]] = [1, regalo]
            else:
                offerte[nomi[0]] = [numero, regalo] 
        except IndexError:
            offerte[nomi[0]] = [numero, regalo] 

    infile.close ()
    return offerte

def calcoloSpesa (carrello, prezzi, offerte):
    totale = 0
    for conchiglia in sorted(carrello):
        quantita = carrello[conchiglia]
        costo = quantita * prezzi[conchiglia]
        try:
            if quantita >= offerte[conchiglia][0]:
                print ("Acquistando", end = " ")
                for i in range (offerte[conchiglia][0]):
                    print (f"{conchiglia},", end = " ")
                print (f"Hai ricevuto {offerte[conchiglia][1]} in regalo")
        except KeyError:
            pass
        totale = totale + costo

    print (totale)
            
def main ():
    carrello = leggiCarrello ("cart.dat")
    prezzi = leggiPrezzi ("prices.dat")
    offerte = leggiOfferte ("offers.dat")
    calcoloSpesa (carrello, prezzi, offerte)

main ()