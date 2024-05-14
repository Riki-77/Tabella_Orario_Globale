def orario_docente(docente):
    file = open('OrarioTabellaGlobale.csv','r')
    campi = next(file)
    ore = next(file)
    count = 0
    for row in file:
        if docente in row:
            riga = row.split(",")
            riga.pop(0)
            for elem in riga:
                if elem !="   ":
                    count += 1
        continue
    file.close()
    return campi, ore, riga, count

#main
docente =input('Inserire il docente: ')
orario = orario_docente(docente)
for parte in orario:
        if parte is orario[3]:
            continue
        else:
            print(parte)
       
print(f'ORE TOTALE DI {docente} SONO {orario[3]}')
