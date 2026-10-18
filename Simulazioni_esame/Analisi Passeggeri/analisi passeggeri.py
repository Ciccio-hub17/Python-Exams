from operator import itemgetter

def leggiFile (filename):
    infile = open (filename, "r")
    origine = {}
    voli = {}

    inutile = infile.readline()
    for line in infile:
        #Michael Jackson,50,M,Chicago,Miami,AA123
        parti = line.split (",")
        citta = parti[3]
        eta = int (parti[1])
        if citta not in origine:
            origine[citta] = [eta]
        else:
            lista = origine[citta]
            lista.append (eta)

        nVolo = parti[-1]
        sesso = parti [2]
        if nVolo not in voli:
            voli [nVolo] = [1, 0, 0]
            if sesso == "M":
                voli[nVolo][1] = voli[nVolo][1] + 1
            else:
                voli[nVolo][2] = voli[nVolo][2] + 1

        else:
            voli [nVolo][0] = voli [nVolo][0] + 1
            if sesso == "M":
                voli[nVolo][1] = voli[nVolo][1] + 1
            else:
                voli[nVolo][2] = voli[nVolo][2] + 1

    infile.close()
    return voli, origine

def stampaVideo (voli, origine):
    print ("Media per le età di ciascuna origine")
    for citta in origine:
        lista = origine[citta]
        media = sum (lista) / len(lista)
        lista.append (media)

    origine = dict (sorted (origine.items(), key = itemgetter(-1), reverse = True))

    for citta in origine:
        media = origine[citta][-1]
        print (f"Origine: {citta}, Media età: {media:.1f}")



    voli = dict(sorted(voli.items(), key = itemgetter(1), reverse = True))

    for idVolo in voli:
        uomini = voli[idVolo][1]
        donne = voli[idVolo][2]
        print(f"Numero di volo più popolare: {idVolo}, Passeggeri M: {uomini} / F: {donne}")
        break

def main ():
    (voli, origine) = leggiFile ("passeggeri.txt")
    stampaVideo (voli, origine)


main ()

