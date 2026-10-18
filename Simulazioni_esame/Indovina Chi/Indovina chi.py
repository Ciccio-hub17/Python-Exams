#Nome;Sesso;Colore Capelli;Lunghezza Capelli;Occhiali;Cappello;Baffi;Barba;Pelato
import copy
def leggiFile (personaggi, domande):
    infilePers = open (personaggi, "r")
    infileDomande = open (domande, "r")
    dictPersonaggi = {}
    dictDomande = {}

    infilePers.readline ()

    for line in infilePers:
        #Alex;Uomo;Nero;Corti;NO;NO;SI;NO;NO
        line = line.strip().split(";")
        tratti = {"Sesso": line[1], "Colore Capelli": line[2], "Lunghezza Capelli": line[3], "Occhiali": line[4], "Cappello": line[5], "Baffi": line[5], "Barba": line[6], "Pelato": line[6],}
        dictPersonaggi [line[0]] = tratti

    for line in infileDomande:
        line = line.strip().split ("=")
        dictDomande[line[0]] = line[1]

    infileDomande.close ()
    infilePers.close ()
    return dictDomande, dictPersonaggi

def gioco (domande, personaggi):
    print (f"Personaggi del gioco: ")

    for personaggio in personaggi:
        print (f"{personaggio} -", end = " ")
        tratti = personaggi[personaggio]
        for caratteristica in tratti:
            print (f"{caratteristica}: {tratti[caratteristica]},", end = " ")
        print ()

    mossa = 1
    dictModificato = dict (personaggi)
    for caratteristica in domande :
        print (f"Mossa {mossa}: - domanda {caratteristica} = {domande[caratteristica]}")
        print ("Personaggi selezionati:")
        for personaggio in personaggi:
            tratti = personaggi[personaggio]
            if tratti[caratteristica] != domande[caratteristica]:
                try:
                    dictModificato.pop (personaggio)
                except KeyError:
                    pass

        for personaggio in dictModificato:
            print (f"{personaggio} -", end = " ")
            tratti = dictModificato[personaggio]
            for caratteristica in tratti:
                print (f"{caratteristica}: {tratti[caratteristica]},", end = " ")

            print ()

        mossa = mossa + 1
    if len (dictModificato) == 1:
        print ("Hai vinto")


def main ():
    dictDomande, dictPersonaggi = leggiFile ("personaggi.txt", "domande1.txt")
    gioco (dictDomande, dictPersonaggi)

main ()