GATE_CONOSCIUTI = ["and", "nand", "or", "nor", "xor", "xnor", "not", "buf"]

GATE_PIU_USCITE = ["and", "nand", "or", "nor", "xor", "xnor"]
GATE_UNA_USCITA = ["not", "buf"]

def leggifile (filename):
    infile = open (filename, "r")

    circuito = []

    for line in infile:
        parti = line.strip().split()
        circuito.append (parti)

    infile.close()
    return circuito

def report_errori (circuito):
    print ("Rilevamento errori")
    #and U1 net1 net2 net3
    totaleErrori = 0

    circuitoSenzaErrori = []
    nomi = set()
    netOutput = set ()
    
    for i in range (len(circuito)):
        controllo = True
        nomePresente = False
        netOutputPresente = False
        if circuito [i][1] not in nomi:
            nomi.add(circuito [i][1])
        else:
            nomePresente = True

        if len (circuito[i]) > 2:
            if circuito [i][2] not in netOutput:
                netOutput.add(circuito [i][2])
            else:
                netOutputPresente = True
       
        if circuito [i][0] not in GATE_CONOSCIUTI:
            print (f"Riga {i}: Gate sconosciuto {circuito [i][0]}")
            totaleErrori = totaleErrori + 1
            controllo = False
        if nomePresente:
            print (f"Riga {i}: Nome già utilizzato {circuito [i][1]}")
            totaleErrori = totaleErrori + 1
            controllo = False
        if circuito[i][0] in GATE_PIU_USCITE:
            if len(circuito[i][3:]) < 2:
                print(f"Riga {i + 1}: Numero di net non valido (meno di 2 ingressi per {circuito[i][0]})")
                totaleErrori += 1
                controllo = False
        elif circuito[i][0] in GATE_UNA_USCITA:
            if len(circuito[i][3:]) != 1:
                print(f"Riga {i + 1}: Numero di net non valido (ingressi per {circuito[i][0]})")
                totaleErrori += 1
                controllo = False
        if netOutputPresente:
            print (f"Riga {i}: net collegata a più output {circuito [i][2]}")
            totaleErrori = totaleErrori + 1
            controllo = False
        if controllo:
            circuitoSenzaErrori.append (circuito[i])

    print ("Totale errori", totaleErrori)

    return (circuitoSenzaErrori, len (nomi))

def input_output (circuitoSenzaErrori):
    input = set ()
    output = set ()

    for i in range (len (circuitoSenzaErrori)):
        numeroInput = circuitoSenzaErrori[i][3:]
        for j in range (len(numeroInput)):
            if numeroInput[j] not in input:
                input.add(numeroInput[j])

        if circuitoSenzaErrori[i][2] not in output:
            output.add(circuitoSenzaErrori[i][2])

    inputGlobali = set ()
    outputGlobali = set ()

    inputGlobali = input - output
    outputGlobali = output - input

        
    print (f"Input globali {len(inputGlobali)}")
    

    print (f"Output globali {len(outputGlobali)}")
    

def statistiche (circuitoSenzaErrori, numeroGate):
    #and U1 net1 net2 net3
    print ("Numero totale dei gate", numeroGate)
    tipo = dict()
    for i in range (len (circuitoSenzaErrori)):
        tipoGate = circuitoSenzaErrori[i][0]
        numerodiInput = len (circuitoSenzaErrori[i][3:])

        if  tipoGate not in tipo:
            tipo[tipoGate] = {}

        if numerodiInput not in tipo[tipoGate]:
            tipo[tipoGate][numerodiInput] = 1
        else:
            tipo[tipoGate][numerodiInput] = tipo[tipoGate][numerodiInput] + 1

    for tipoGate in tipo:
        for numeroInput in tipo[tipoGate]:
            print (f"{tipo[tipoGate][numeroInput]} {tipoGate} con {numeroInput} input")
            

def main ():
    ok = False
    while not ok:
        try:
            filename = input ("Dammi il nome del file: ")
            circuito = leggifile (filename)
            ok = True
            (circuitoSenzaErrori, numeroGate) = report_errori(circuito)
            input_output(circuitoSenzaErrori)
            statistiche (circuitoSenzaErrori, numeroGate)
        except FileNotFoundError:
            print ("Impossibile trovare il file, riprova")

main()