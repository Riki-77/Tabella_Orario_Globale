def cognome_nome(nome):
    file=open('OrarioTabellaGlobale.csv', 'r')
    filecsv=csv.reader(file) #apre il file csv
    for row in filecsv: #cerca quante volte "D" è presente nella riga del docente inserito
        if nome in row[0]:
            contatore=0
            for ora in row:
                if ' D' in ora: #spazio prima di D per non prendere D sbagliate come ad esempio le classi
                    contatore+=1
            break
    return contatore