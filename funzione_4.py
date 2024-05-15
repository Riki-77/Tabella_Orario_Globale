def docenti_lezione_ora(giorno, ora):
    # Open the file in read mode using a with statement
    F = open('OrarioTabellaGlobale.csv', 'r') as file:
        # Read the first two rows (header fields and time slots)
        intestazioni_giorni = next(file).strip().split(',')
        ore_giorni = next(file).strip().split(',')

        # Remove any leading/trailing whitespace from the elements in the lists
        intestazioni_giorni = [x.strip().lower() for x in intestazioni_giorni]
        ore_giorni = [x.strip().lower() for x in ore_giorni]

        # Find the indices that correspond to the given day and time
        indici_richiesti = []
        for i in range(1, len(intestazioni_giorni)):  # Start from 1 to skip the "Docente" column
            if intestazioni_giorni[i] == giorno.lower() and ore_giorni[i] == ora.lower():
                indici_richiesti.append(i)

        # Find the teachers who have a lesson in the found indices
        elenco_docenti = []
        for row in file:
            riga = row.strip().split(',')
            docente = riga[0].strip()
            for indice in indici_richiesti:
                if len(riga) > indice and riga[indice].strip() != "":
                    elenco_docenti.append(docente)
                    break
    
    # Return the list of teachers and the total number of teachers
    return elenco_docenti, len(elenco_docenti)

# Main
# Prompt the user to enter the day and time
giorno = input('Inserire il giorno della settimana (es. lu): ').strip()
ora = input('Inserire l\'ora (es. 1): ').strip()

# Call the function and get the list of teachers and the total number
elenco_docenti, totale_docenti = docenti_lezione_ora(giorno, ora)

# Print the list of teachers if there are any, otherwise print a message
if elenco_docenti:
    print(f'I docenti che hanno lezione nella {ora} del {giorno} sono:')
    for docente in elenco_docenti:
        print(docente)
else:
    print(f'Non ci sono docenti che hanno lezione nella {ora} del {giorno}.')

# Print the total number of teachers
print(f'Numero totale dei docenti che hanno lezione nell\'ora specificata: {totale_docenti}')
