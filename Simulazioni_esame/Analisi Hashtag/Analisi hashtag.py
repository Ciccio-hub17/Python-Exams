def leggiFile (filename):
    infile = open (filename, "r")

    dizionario1 = {}
    dizionario2 = {}

    for line in infile:
        parti = line.split ()
        data = parti[0].split("-")
        giorno = data[2]
        hashtag = parti[2:]
        if giorno == "01":
            for i in range (len (hashtag)):
                if hashtag[i] not in dizionario1:
                    dizionario1[hashtag[i]] = 1
                else:
                    dizionario1[hashtag[i]] = dizionario1[hashtag[i]] + 1
        else:
            for i in range (len (hashtag)):
                if hashtag[i] not in dizionario2:
                    dizionario2[hashtag[i]] = 1
                else:
                    dizionario2[hashtag[i]] = dizionario2[hashtag[i]] + 1

    infile.close()
    print (dizionario1)
    print (dizionario2)
    return dizionario1, dizionario2

def controllo (dizionario1, dizionario2):
    print ("hashtag in tendenza")
    for hashtag in dizionario1:
        if hashtag in dizionario2:
            incremento = dizionario2[hashtag] * 100 / dizionario1[hashtag]
            incremento = round (incremento - 100) 
            if incremento >= 50:
                print (f"{hashtag} con un incremento del {incremento}%")

def main ():
    try:
        dizionario1, dizionario2 = leggiFile ("hashtags.csv")
        controllo (dizionario1, dizionario2)
    except FileNotFoundError:
        print ("Impossibile trovare il file")
    except KeyError:
        print ("errore nella gestione del dizionario")


main ()