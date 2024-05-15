def orario_docente(docente):
    # Open the file in read mode
    file = open('OrarioTabellaGlobale.csv','r')
    
    # Read the first two rows (header fields and time slots)
    campi = next(file)
    ore = next(file)
    
    # Initialize a counter for the total number of hours
    count = 0
    
    # Iterate through the remaining rows
    for row in file:
        # Check if the given teacher is in the row
        if docente in row:
            # Split the row into a list of elements
            riga = row.split(",")
            
            # Remove the first element (the teacher's name)
            riga.pop(0)
            
            # Iterate through the remaining elements in the row
            for elem in riga:
                # Check if the element is not empty
                if elem !="   ":
                    # Increment the counter
                    count += 1
        
        # Continue to the next row
        continue
    
    # Close the file
    file.close()
    
    # Return the header fields, time slots, row of data, and total number of hours
    return campi, ore, riga, count

# Main
# Prompt the user to enter the teacher's name
docente =input('Inserire il docente: ')

# Call the function and store the returned values
orario = orario_docente(docente)

# Iterate through the returned values, except for the total number of hours
for parte in orario:
    if parte is orario[3]:
        continue
    else:
        print(parte)
       
# Print the total number of hours for the given teacher
print(f'ORE TOTALE DI {docente} SONO {orario[3]}')
