import math

# Funzione per calcolare la distanza euclidea tra due punti
def distanza(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Caricamento dei dati da 'survivors.txt'
def carica_sopravvissuti(file):
    sopravvissuti = []
    with open(file, 'r', encoding='utf-8') as f:
        next(f)  # Salta l'intestazione
        for line in f:
            data = line.strip().split(',')
            id = int(data[0])
            x = int(data[1])
            y = int(data[2])
            speed = float(data[3])
            endurance = int(data[4])
            sopravvissuti.append([id, x, y, speed, endurance])
    return sopravvissuti

# Caricamento dei dati da 'desert.csv'
def carica_oasi(file):
    oasi = []
    with open(file, 'r', encoding='utf-8') as f:
        next(f)  # Salta l'intestazione
        for line in f:
            data = line.strip().split(',')
            x = int(data[0])
            y = int(data[1])
            oasi.append((x, y))
    return oasi

# Simulazione della sopravvivenza degli esploratori
def simula_sopravvivenza(sopravvissuti, oasi):
    sopravvissuti_count = 0
    morti = []
    
    for esploratore in sopravvissuti:
        id, x, y, speed, endurance = esploratore
        distanza_massima = speed * endurance
        oasi_visitata = []
        uscito = False
        morto = False

        # Verifica se l'esploratore può uscire dal deserto in un giorno
        if x >= 500 - distanza_massima or y >= 500 - distanza_massima or x <= distanza_massima or y <= distanza_massima:
            uscito = True
        
        # Se non può uscire, cerca la oasi più vicina
        while not uscito and not morto:
            oasi_più_vicina = None
            distanza_minima = float('inf')

            for oasi_x, oasi_y in oasi:
                if (oasi_x, oasi_y) not in oasi_visitata:
                    dist = distanza(x, y, oasi_x, oasi_y)
                    if dist <= distanza_massima and dist < distanza_minima:
                        distanza_minima = dist
                        oasi_più_vicina = (oasi_x, oasi_y)

            if oasi_più_vicina:
                oasi_visitata.append(oasi_più_vicina)
                x, y = oasi_più_vicina  # L'esploratore si sposta alla nuova oasi

                # Dopo il riposo nell'oasi, verifica se l'esploratore può uscire
                if x >= 500 - distanza_massima or y >= 500 - distanza_massima or x <= distanza_massima or y <= distanza_massima:
                    uscito = True
            else:
                ultima_oasi = oasi_visitata[-1] if oasi_visitata else (x, y)
                morti.append((id, ultima_oasi))
                morto = True

        if uscito:
            sopravvissuti_count += 1

    # Calcolare la percentuale di sopravvissuti
    percentuale_sopravvissuti = (sopravvissuti_count / len(sopravvissuti)) * 100
    
    return percentuale_sopravvissuti, morti

# Funzione principale per eseguire il programma
def main():
    sopravvissuti = carica_sopravvissuti('survivors.txt')
    oasi = carica_oasi('desert.csv')

    percentuale_sopravvissuti, morti = simula_sopravvivenza(sopravvissuti, oasi)

    # Stampa dei risultati
    print(f"Sopravvissuti: {percentuale_sopravvissuti:.2f}%")
    
    if morti:
        print("Recupero salme esploratori")
        for morto in morti:
            id, ultima_oasi = morto
            print(f"<{id}>: {ultima_oasi}")

# Esegui il programma
if __name__ == '__main__':
    main()
