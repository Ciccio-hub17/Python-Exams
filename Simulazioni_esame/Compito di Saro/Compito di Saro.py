from csv import reader
from operator import itemgetter
NOMEFILE = "testocsv.csv"

def creazione(filename):
    infile = open(filename, "r")
    csvReader = reader(infile)
    next(csvReader)

    indicatori = dict()
    table = []
    indice = 0
    insieme = set()
    for line in csvReader:
        table.append(line)
        if line[5] not in insieme:
            insieme.add (line[5])
      
    for element in insieme:
        indicatori[indice + 1] = element
        indice = indice + 1
    
    print ("Indicatori della qualità della vita")
    for key in indicatori:
        print (f"{key}. {indicatori[key]}")

    ok = False
    while not ok:
        try:
            numeroIndicatore = int (input ("ciao, ecco a te tutti gli indicatori, scegline 1: "))
            ok = True
        except ValueError:
            print ("Il numero non è convertibile")

    visualizzazione (table, indicatori, numeroIndicatore)
    infile.close()

def visualizzazione(table, indicatori, numeroIndicatore):
    record = []
    for i in range (len (table)):
        if indicatori[numeroIndicatore] == table[i][5]:
            record.append((table[i][3], table[i][4]))

    record = sorted (record, key = itemgetter(1), reverse = True)
    for element in record:
        print (f"{element[0]}: {element[1]}")

def main ():
    try:
        indicatori = creazione (NOMEFILE)
    except FileNotFoundError:
        print ("Impossibile trovare il file")

main ()