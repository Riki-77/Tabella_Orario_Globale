#elenco docenti di una data classe
import pydoc

#funzione
def elenco_docenti(classe):
    '''
Ritorna l'elenco dei docenti di una classe data.

Args:
    classe (string): classe data dall'utente
    
Returns:
    elenco : elenco docenti della classe
    '''
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file)
    ore = next(file)
    elenco = [] #elenco docenti vuoto
    uscita = True
    while uscita == True:
        riga = file.readline()
        if riga != '': #esegue fino alla fine del file
            if classe in riga: #se la classe è nella riga viene aggiunto all'elenco il primo elemento della riga (nome docente)       
                parti = riga.split(',')
                elenco.append(parti[0])
            else:
                continue
        else:
            uscita = False
    file.close() #chiusura file
    return elenco

#while True: #loop infinito
    #input utente
    in_classe = input('Inserire la classe : ').upper()

    #chiamata funzione
    docenti = elenco_docenti(in_classe)

    #stampa risultato
    print(f'I docenti della classe {in_classe} sono:')
    for elem in docenti:
        print(elem)
    print('\n')