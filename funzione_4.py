def docenti_lezione_ora(giorno, ora):
    file = open('OrarioTabellaGlobale.csv','r')
    campi = next(file)
    ore = next(file)
    elenco_docenti = []
    for row in file:
        riga = row.split(",")
        if riga[1].strip() == giorno and riga[2].strip() == ora:
            for elem in riga[3:]:
                if elem.strip() != "":
                    elenco_docenti.append(elem.strip())
    file.close()
    return campi, ore, elenco_docenti, len(elenco_docenti)

#main
giorno = input('Inserire il giorno della settimana (es. lunedì): ')
ora = input('Inserire l\'ora (es. prima ora): ')
orario_lezione = docenti_lezione_ora(giorno, ora)
for parte in orario_lezione:
    if parte is orario_lezione[3]:
        continue
    else:
        print(parte)
print(f'Numero totale dei docenti che hanno lezione nell\'ora specificata: {orario_lezione[3]}')
