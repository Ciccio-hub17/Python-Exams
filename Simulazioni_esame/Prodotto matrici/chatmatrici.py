def leggi_matrici(file):
    matrici = []
    with open(file, 'r') as f:
        for line in f:
            valori = list(map(int, line.split()))
            r, c = valori[0], valori[1]
            matrice = [valori[i:i+c] for i in range(2, len(valori), c)]
            matrici.append((matrice, r, c))
    return matrici

def moltiplica_matrici(A, B):
    """Moltiplica due matrici A e B manualmente."""
    m = len(A)    # Numero di righe di A
    n = len(A[0]) # Numero di colonne di A (uguale al numero di righe di B)
    p = len(B[0]) # Numero di colonne di B
    
    # Inizializza la matrice risultato con zeri
    C = [[0] * p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def prodotto_matrici(matrici):
    while len(matrici) > 1:
        # Troviamo la coppia di matrici da moltiplicare con il minor costo computazionale
        min_costo = float('inf')
        best_pair = (0, 1)

        for i in range(len(matrici) - 1):
            A, rA, cA = matrici[i]
            B, rB, cB = matrici[i + 1]
            costo = rA * cA * cB  # operazioni per moltiplicare A (rA x cA) e B (rB x cB)
            if costo < min_costo:
                min_costo = costo
                best_pair = (i, i + 1)

        # Moltiplica le due matrici selezionate
        i, j = best_pair
        A, rA, cA = matrici[i]
        B, rB, cB = matrici[j]
        
        # Verifica compatibilità delle dimensioni
        if cA != rB:
            print("Impossibile calcolare il prodotto - le dimensioni non coincidono")
            return

        print(f"Moltiplicazione delle matrici con dimensioni ({rA}, {cA}) e ({rB}, {cB}) -> ({rA}, {cB})")

        # Calcola il prodotto
        C = moltiplica_matrici(A, B)
        
        # Sostituisci le due matrici con il risultato
        matrici[i] = (C, rA, cB)
        del matrici[j]

    return matrici[0][0]

def main():
    # File con le matrici da leggere
    file_matrici = 'matrices.txt'

    # Leggi le matrici dal file
    matrici = leggi_matrici(file_matrici)

    # Verifica le dimensioni iniziali delle matrici
    print("Matrici da moltiplicare:", end=" ")
    print(", ".join([f"{r} x {c}" for _, r, c in matrici]))

    # Calcola il prodotto delle matrici
    risultato = prodotto_matrici(matrici)

    # Stampa la matrice risultante con la formattazione richiesta
    print("\nRisultato:")
    for riga in risultato:
        print(" ".join([f"{v:12d}" for v in riga]))

if __name__ == "__main__":
    main()
