def read_and_analyze_grades():
    # Initialize variables to track total, count, and individual grades
    total = 0
    count = 0
    grades = []

    try:
        # Open the 'grades.txt' file in read mode
        with open('grades.txt', 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Process each line, removing extra whitespace and calculating totals
            for line in lines:
                grade = line.strip()  # Remove any extra whitespace or newlines
                
                if grade:  # Ensure the line is not empty
                    grade = float(grade)
                    grades.append(grade)  # Add grade to list
                    total += grade  # Increment count (since each line is a grade)
                    count += 1
        
        # Calculate average
        if total > 0:
            average = total / len(grades)  # Average = total grades / number of grades
        else:
            average = 0

        # Display the results
        print("Grades in the file:")

        for grade in grades:
            print(grade)

        print(f"\nGrade total: {total}")
        print(f"\nTotal number of grades: {count}")
        print(f"Average of grades: {average:.2f}")

    except FileNotFoundError:
        print("Error: 'grades.txt' file not found.")

# Run the function to read and analyze grades
read_and_analyze_grades()

