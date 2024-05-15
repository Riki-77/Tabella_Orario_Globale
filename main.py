def main():
    print()
    x = int(input('''
1. Elenco dei docenti di una data classe.
2. Orario di un determinato docente e numero totale delle ore del docente.
3. Cognome e nome di un determinato docente e numero di ore a disposizione.
4. Elenco dei docenti che hanno lezione una determinata ora di un determinato giorno della settimana e numero totale dei docenti.
Inserire il numero della funzione desiderata:'''))
    if x == 1:
        classe = input('Inserire la classe : ')
        from F1 import elenco_docenti  
        docenti = elenco_docenti(classe)
        print(f'I docenti della classe {classe} sono:')
        for elem in docenti:
            print(elem.strip())
    elif x == 2:  
        docente = input('Inserire il docente: ')
        from F2 import Tabella_docente 
        orario = Tabella_docente(docente)
        for parte in orario:
            if parte is orario[3]:
                continue
            else:
                print(parte)
    elif x == 3:
        docente = input('Inserire il docente: ')
        from F3 import orario_docente 
        orario = orario_docente(docente)
        print(f'ORE TOTALE DI {docente} SONO {orario[3]}')
   
    elif x== 4:
        giorno = input('Inserire il giorno della settimana (es. lu): ').strip()
        ora = input('Inserire l\'ora (es. 1): ').strip()
        from F4 import docenti_lezione_ora  
        elenco_docenti, totale_docenti = docenti_lezione_ora(giorno, ora)
        print(f'I docenti che hanno lezione nella {ora} del {giorno} sono:')
        for docente in elenco_docenti:
            print(docente)
        print(f'Numero totale dei docenti che hanno lezione nell\'ora specificata: {totale_docenti}')


main()