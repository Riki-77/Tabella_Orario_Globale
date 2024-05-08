def classe(clas):
    file=open('OrarioTabellaGlobale.csv', 'r')
    filecsv=csv.reader(file) #apre il file csv
    docenti=[] #lista per poter salvare i nomi dei docenti della classe immessa
    for row in filecsv: #se trova la classe inserita in una riga, aggiunge i docenti nella lista "docenti"
        if clas in row:
            docenti.append(row[0])
    return docenti