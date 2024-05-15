def get_teacher_schedule(teacher_name):
    """
    Retrieves the schedule for a given teacher from the 'OrarioTabellaGlobale.csv' file.

    Args:
        teacher_name (str): The name of the teacher.

    Returns:
        tuple: A tuple containing the teacher's schedule and the total number of teaching hours.
    """
    F = open('OrarioTabellaGlobale.csv', 'r'):
        # Skip the first two rows (header and time slots)
        next(file)
        next(file)

        teacher_schedule = []
        total_hours = 0
        for row in file:
            if teacher_name in row:
                row_data = row.split(",")
                row_data.pop(0)  # Remove the teacher's name
                for cell in row_data:
                    if cell.strip() != "   ":
                        teacher_schedule.append(cell.strip())
                        total_hours += 1

    return teacher_schedule, total_hours

# Example usage
teacher_name = input('Enter the teacher name: ')
schedule, total_hours = get_teacher_schedule(teacher_name)
print(f"Total teaching hours for {teacher_name}: {total_hours}")
