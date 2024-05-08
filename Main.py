def main():
    print('''MENU
Inserire il numero della funzione desiderata:
1. Elenco dei docenti di una data classe.
2. Orario di un determinato docente e numero totale delle ore del docente.
3. Cognome e nome di un determinato docente e numero di ore a disposizione.
4. Elenco dei docenti che hanno lezione una determinata ora di un determinato giorno della settimana e numero totale dei docenti.''')
    menu=input(">> ")
    if (menu=="1"):
        clas=input("Inserire la classe di cui si vogliono sapere i docenti: ")
        c=classe(clas)
        print(f"I docenti per la classe {clas} sono: ")
        for elemento in c: #serve per poter scrivere un docente per riga
            print(elemento)
    if (menu=="2"):
        doc=input("Inserire il docente di cui si vuole sapere il numero totale di ore e il suo orario: ")
        d=docente(doc)
        print(d)
    if (menu=='3'):
        nome=input("Inserire il cognome e nome del docente di cui si vuole sapere il numero di ore a disposizione: ")
        c=cognome_nome(nome)
        print(f"Le ore a disposizione di {nome} sono {c}.")
    if (menu=='4'):
        elen=input("Inserire il giorno e ora di cui si vuole sapere l'elenco dei professori che hanno lezione: ")
        e=elenco(elen)
        print("L'elenco dei professori per il giorno e ora {elen} sono:")
        for elemento in e: #serve per poter scrivere un docente per riga creando un elenco
            print(elemento)
    return

main()