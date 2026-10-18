GATE_CONOSCIUTI = ["and", "nand", "or", "nor", "xor", "xnor", "not", "buf"]
GATE_PIU_USCITE = ["and", "nand", "or", "nor", "xor", "xnor"]
GATE_UNA_USCITA = ["not", "buf"]

def leggifile(filename):
    # Leggi il file e ritorna il circuito come lista di righe.
    try:
        with open(filename, "r") as infile:
            circuito = [line.strip().split() for line in infile]
        return circuito
    except FileNotFoundError:
        print("File non trovato!")
        return []

def report_errori(circuito):
    print("Rilevamento errori")
    totaleErrori = 0
    circuitoSenzaErrori = []
    nomi = set()
    netOutput = set()
    nets_collegate_a_uscite = {}

    for i, line in enumerate(circuito):
        controllo = True
        nomePresente = False
        netOutputPresente = False
        
        if len(line) < 2:
            print(f"Riga {i + 1}: Formato non valido")
            totaleErrori += 1
            continue
        
        tipo_gate = line[0]
        nome_gate = line[1]
        net_output = line[2] if len(line) > 2 else None
        ingressi = line[3:] if len(line) > 3 else []

        # Verifica gate sconosciuto
        if tipo_gate not in GATE_CONOSCIUTI:
            print(f"Riga {i + 1}: Gate sconosciuto {tipo_gate}")
            totaleErrori += 1
            controllo = False
        
        # Verifica nome già utilizzato
        if nome_gate in nomi:
            print(f"Riga {i + 1}: Nome già utilizzato {nome_gate}")
            totaleErrori += 1
            controllo = False
        else:
            nomi.add(nome_gate)

        # Verifica net collegata a più output
        if net_output and net_output in netOutput:
            print(f"Riga {i + 1}: Net collegata a più output {net_output}")
            totaleErrori += 1
            controllo = False
        else:
            if net_output:
                netOutput.add(net_output)
        
        # Verifica numero di ingressi
        if tipo_gate in GATE_PIU_USCITE:
            if len(ingressi) < 2:
                print(f"Riga {i + 1}: Numero di net non valido (meno di 2 ingressi per {tipo_gate})")
                totaleErrori += 1
                controllo = False
        elif tipo_gate in GATE_UNA_USCITA:
            if len(ingressi) != 1:
                print(f"Riga {i + 1}: Numero di net non valido (ingressi per {tipo_gate})")
                totaleErrori += 1
                controllo = False

        # Se non ci sono errori, aggiungi al circuito senza errori
        if controllo:
            circuitoSenzaErrori.append(line)
    
    print(f"Totale errori: {totaleErrori}")
    return circuitoSenzaErrori, len(nomi)

def input_output(circuitoSenzaErrori):
    input_set = set()
    output_set = set()

    # Aggiungi le net di input e output globali
    for line in circuitoSenzaErrori:
        net_output = line[2] if len(line) > 2 else None
        ingressi = line[3:] if len(line) > 3 else []

        # Se la net è in ingresso, aggiungila
        for net in ingressi:
            input_set.add(net)
        
        # Se la net è in uscita, aggiungila
        if net_output:
            output_set.add(net_output)
    
    # Identifica gli input globali (presenti come ingressi ma non come uscite)
    global_input = input_set - output_set
    # Identifica gli output globali (presenti come uscite ma non come ingressi)
    global_output = output_set - input_set

    print(f"Input globali {len(global_input)}")
    for net in sorted(global_input):
        print(net)

    print(f"Output globali {len(global_output)}")
    for net in sorted(global_output):
        print(net)

def statistiche(circuitoSenzaErrori):
    print("Statistiche:")
    gate_count = len(circuitoSenzaErrori)
    tipo_gate_count = {}

    for line in circuitoSenzaErrori:
        tipo_gate = line[0]
        num_ingressi = len(line[3:])

        # Conta il numero di gate per tipo
        if tipo_gate not in tipo_gate_count:
            tipo_gate_count[tipo_gate] = {}

        if num_ingressi not in tipo_gate_count[tipo_gate]:
            tipo_gate_count[tipo_gate][num_ingressi] = 1
        else:
            tipo_gate_count[tipo_gate][num_ingressi] += 1

    print(f"Numero totale dei gate: {gate_count}")
    for tipo_gate, ingressi_count in tipo_gate_count.items():
        for num_ingressi, count in ingressi_count.items():
            print(f"{count} {tipo_gate} con {num_ingressi} input")

def main():
    while True:
        try:
            filename = input("Dammi il nome del file: ")
            circuito = leggifile(filename)
            if not circuito:
                continue
            circuitoSenzaErrori, numero_gate = report_errori(circuito)
            input_output(circuitoSenzaErrori)
            statistiche(circuitoSenzaErrori)
            break
        except Exception as e:
            print(f"Errore: {e}")

main()
