def leggiLingue (filename):
    lingue = {}
    infile = open (filename, "r")

    for line in infile:
        line = line.strip().split(",")
        lingue [line[0]] = line[1:]

    infile.close ()
    return lingue

def leggiViaggi(filename):
    viaggi = {}
    infile = open (filename, "r")

    for line in infile: 
        line = line.strip().split(",")
        viaggi[line[0]] = [int(line[1]), int(line[2])]

    infile.close ()
    return viaggi

def stampa (lingue, viaggi):
    somma = 0
    passeggeri = 0
    lista = []
    for pianeta in viaggi:
        somma = somma + viaggi[pianeta][0]
        passeggeri = passeggeri + viaggi[pianeta][1]
    
    media = round (somma /len(viaggi), 2)
    print (f"Durata media dei viaggi: {media}")
    print (f"Numero totale dei passeggeri: {passeggeri}")

    print (f"Lingue parlate su ciascun pianeta visitato:")

    for pianeta in viaggi:
        print (f"{pianeta} : {lingue[pianeta]}")
        for i in range (len (lingue[pianeta])):
            lista.append (lingue[pianeta][i])
    
    linguePiuParlate = {}
    for i in range (len (lista)):
        if lista[i] not in linguePiuParlate:
            linguePiuParlate [lista[i]] = 1
        else:
            linguePiuParlate [lista[i]] = linguePiuParlate [lista[i]] + 1

    linguePiuParlate = sorted (linguePiuParlate.items (), key = lambda x:x[1], reverse=True)

    i = 0
    print (f"Tre lingue più ricorrenti tra i pianeti visitati: [", end = "")
    for i in range (3):
        if i != 2:
            print (f"'{linguePiuParlate[i][0]}', ", end = "")
        else:
            print (f"'{linguePiuParlate[i][0]}'", end = "")
    print ("]")

            

    
    



def main ():
    lingue = leggiLingue ("lingue_pianeti.txt")
    viaggi = leggiViaggi ("viaggi_enterprise.txt")
    stampa (lingue, viaggi)

main ()