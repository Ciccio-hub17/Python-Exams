import random

FILENAME = "qualificati.txt"

def lettura (filename):
    infile = open(filename, "r")
    giocatori = dict()
    for line in infile:
        line = line.strip()
        parts = line.split(",")
        parts[0] = int(parts[0])
        giocatori[parts[0]] = parts[1]

    infile.close()
    return giocatori
    
def creazioneOutput(giocatori):
    gironeVerde = open ("verde.txt", "w")
    gironeRosso = open ("rosso.txt", "w")
    calendario = open ("calendario.txt", "w")

    giocatoriPerGirone = dict (giocatori)

    gironeVerde.write (f"1 - {giocatoriPerGirone[1]} \n")
    gironeRosso.write (f"2 - {giocatoriPerGirone[2]} \n")

    tabellaGironeVerde = []
    tabellaGironeRosso = []

    listaPerVerde = []
    listaPerRosso = []
    
    listaPerVerde.append (1)
    listaPerVerde.append (giocatoriPerGirone[1])

    listaPerRosso.append (2)
    listaPerRosso.append (giocatoriPerGirone[2])

    tabellaGironeVerde.append(listaPerVerde)
    tabellaGironeRosso.append (listaPerRosso)

    giocatoriPerGirone.pop(1)
    giocatoriPerGirone.pop(2)

    print (giocatoriPerGirone)

    chiavi = []
    for key in giocatoriPerGirone:
        chiavi.append(key)

    for i in range (3):
        listaVerde = []
        listaRosso = []
        estratto = random.choice (chiavi)
        gironeVerde.write (f"{estratto} - {giocatoriPerGirone[estratto]} \n")
        listaVerde.append (estratto)
        listaVerde.append(giocatoriPerGirone[estratto])

        if estratto % 2 == 0:
            estrattoNuovo = estratto - 1
        else:
            estrattoNuovo = estratto + 1

        gironeRosso.write (f"{estrattoNuovo} - {giocatoriPerGirone[estrattoNuovo]} \n")
        listaRosso.append (estrattoNuovo)
        listaRosso.append(giocatoriPerGirone[estrattoNuovo])

        chiavi.remove(estratto)
        chiavi.remove(estrattoNuovo)

        giocatoriPerGirone.pop(estratto)
        giocatoriPerGirone.pop(estrattoNuovo)

        tabellaGironeVerde.append (listaVerde)
        tabellaGironeRosso.append(listaRosso)

    print (tabellaGironeVerde)
    print (tabellaGironeRosso)
    calendario.write("GIRONE VERDE \n")
    for i in range (1, 4):
        calendario.write(f"GIORNATA {i} \n")
        if i == 1:
            calendario.write(f"{tabellaGironeVerde[0][1]} vs {tabellaGironeVerde[-1][1]} \n")
            calendario.write(f"{tabellaGironeVerde[1][1]} vs {tabellaGironeVerde[-2][1]} \n")
        elif i == 2:
            calendario.write(f"{tabellaGironeVerde[0][1]} vs {tabellaGironeVerde[-2][1]} \n")
            calendario.write(f"{tabellaGironeVerde[1][1]} vs {tabellaGironeVerde[-1][1]} \n")
        else:
            calendario.write(f"{tabellaGironeVerde[0][1]} vs {tabellaGironeVerde[1][1]} \n")
            calendario.write(f"{tabellaGironeVerde[-1][1]} vs {tabellaGironeVerde[-2][1]} \n")
    
    calendario.write ("GIRONE ROSSO \n")

    for i in range (1, 4):
        calendario.write(f"GIORNATA {i} \n")
        if i == 1:
            calendario.write(f"{tabellaGironeRosso[0][1]} vs {tabellaGironeRosso[-1][1]} \n")
            calendario.write(f"{tabellaGironeRosso[1][1]} vs {tabellaGironeRosso[-2][1]} \n")
        elif i == 2:
            calendario.write(f"{tabellaGironeRosso[0][1]} vs {tabellaGironeRosso[-2][1]} \n")
            calendario.write(f"{tabellaGironeRosso[1][1]} vs {tabellaGironeRosso[-1][1]} \n")
        else:
            calendario.write(f"{tabellaGironeRosso[0][1]} vs {tabellaGironeRosso[1][1]} \n")
            calendario.write(f"{tabellaGironeRosso[-1][1]} vs {tabellaGironeRosso[-2][1]} \n")
        
    gironeVerde.close()
    gironeRosso.close()
    calendario.close()

def main ():

    giocatori = lettura(FILENAME)

    creazioneOutput (giocatori)

main ()