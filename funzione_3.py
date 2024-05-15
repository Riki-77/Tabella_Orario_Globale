def orario_docente(docente):
    # Open the CSV file
    file = open('OrarioTabellaGlobale.csv','r')
    
    # Read the header fields and time slots
    campi = next(file)
    ore = next(file)
    
    # Initialize a counter for the total number of teaching hours
    count = 0
    
    # Iterate through the rows in the file
    for row in file:
        # Check if the current row contains the teacher's name
        if docente in row:
            # Split the row into individual cells
            riga = row.split(",")
            # Remove the teacher's name from the row data
            riga.pop(0)
            # Iterate through the cells in the row
            for elem in riga:
                # Check if the cell is not empty
                if elem !="   ":
                    # Increment the total number of teaching hours
                    count += 1
        # Continue to the next row
        continue
    
    # Close the file
    file.close()
    
    # Return the header fields, time slots, teacher's schedule, and total number of teaching hours
    return campi, ore, riga, count

#main
#docente =input('Inserire il docente: ') 
#orario = orario_docente(docente)
#print(f'ORE TOTALE DI {docente} SONO {orario[3]}')
