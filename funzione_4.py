def docenti_lezione_ora(giorno, ora):
    with open('OrarioTabellaGlobale.csv', 'r') as file:
        # Leggi le prime due righe
        intestazioni_giorni = next(file).strip().split(',')
        ore_giorni = next(file).strip().split(',')

        # Rimuovi eventuali spazi bianchi attorno agli elementi
        intestazioni_giorni = [x.strip().lower() for x in intestazioni_giorni]
        ore_giorni = [x.strip().lower() for x in ore_giorni]

        # Trova gli indici che corrispondono al giorno e all'ora specificati
        indici_richiesti = []
        for i in range(1, len(intestazioni_giorni)):  # Inizia da 1 per saltare la colonna "Docente"
            if intestazioni_giorni[i] == giorno.lower() and ore_giorni[i] == ora.lower():
                indici_richiesti.append(i)

        # Cerca i docenti che hanno lezione negli indici trovati
        elenco_docenti = []
        for row in file:
            riga = row.strip().split(',')
            docente = riga[0].strip()
            for indice in indici_richiesti:
                if len(riga) > indice and riga[indice].strip() != "":
                    elenco_docenti.append(docente)
                    break
    
    return elenco_docenti, len(elenco_docenti)

# Main
giorno = input('Inserire il giorno della settimana (es. lu): ').strip()
ora = input('Inserire l\'ora (es. 1): ').strip()
elenco_docenti, totale_docenti = docenti_lezione_ora(giorno, ora)

if elenco_docenti:
    print(f'I docenti che hanno lezione nella {ora} del {giorno} sono:')
    for docente in elenco_docenti:
        print(docente)
else:
    print(f'Non ci sono docenti che hanno lezione nella {ora} del {giorno}.')

print(f'Numero totale dei docenti che hanno lezione nell\'ora specificata: {totale_docenti}')
