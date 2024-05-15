def get_teacher_schedule(teacher_name):
    """
    Retrieves the schedule for a given teacher from the 'OrarioTabellaGlobale.csv' file.
    
    Args:
        teacher_name (str): The name of the teacher.
    
    Returns:
        tuple: A tuple containing the teacher's schedule and the total number of teaching hours.
    """
    # Open the file in read mode
    f = open('OrarioTabellaGlobale.csv', 'r'):
        # Skip the first two rows (header and time slots)
        next(file)
        next(file)
        
        # Initialize lists to store the teacher's schedule and total hours
        teacher_schedule = []
        total_hours = 0
        
        # Iterate through the remaining rows
        for row in file:
            # Check if the teacher's name is in the row
            if teacher_name in row:
                # Split the row into a list of elements
                row_data = row.split(",")
                
                # Remove the teacher's name from the list
                row_data.pop(0)
                
                # Iterate through the remaining elements in the row
                for cell in row_data:
                    # Check if the cell is not empty
                    if cell.strip() != "   ":
                        # Add the cell to the teacher's schedule and increment the total hours
                        teacher_schedule.append(cell.strip())
                        total_hours += 1
    
    # Return the teacher's schedule and total hours
    return teacher_schedule, total_hours

# Main
# Prompt the user to enter the teacher's name
teacher_name = input('Enter the teacher name: ')

# Call the function and store the returned values
schedule, total_hours = get_teacher_schedule(teacher_name)

# Print the total teaching hours for the given teacher
print(f"Total teaching hours for {teacher_name}: {total_hours}")
