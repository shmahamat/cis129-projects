
def is_valid_grade(grade):
    
    if  grade == 'done':
        return False

    if grade.isdigit():
        if float(grade) <= 100 and float(grade) >= 0:
            return False
        else:
            return True

    try:
        float(grade)
    except:
        return True
    
    if float(grade) <= 100 and float(grade) >= 0:
        return False
    else:
        return True

    return False

        
def store_grades():
    # Open the 'grades.txt' file in append mode
    with open('grades.txt', 'a') as file:
        
        grade = input("Enter a grade (or type 'done' to finish): ")
        
        while is_valid_grade(grade):
        
            # Ask the user for a grade input
            grade = input("Enter a grade (or type 'done' to finish): ")
            
            if grade.lower() == 'done':
                print("Exiting and saving grades.")
                break

        # Write the grade to the file
        if grade != 'done':
            file.write(grade + '\n')
            print(f"Grade {grade} has been saved.")
        
        return grade

# Run the function
grade = 0
while grade != 'done':
    grade = store_grades()
    
