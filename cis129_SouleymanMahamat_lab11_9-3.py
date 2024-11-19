import csv

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


def enter_grades():
    
    # Open the 'grades.csv' file in write mode
    with open('grades.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        while True:
            # Get the student's first name, last name, and exam grades
            first_name = input("Enter student's first name (or type 'done' to finish): ")
            if first_name.lower() == 'done':
                print("Exiting and saving grades.")
                grade = 'done'
                return grade

            last_name = input("Enter student's last name: ")
            
            try:
                exam1_grade = float(input("Enter grade for exam 1: "))
                exam2_grade = float(input("Enter grade for exam 2: "))
                exam3_grade = float(input("Enter grade for exam 3: "))
            except ValueError:
                print("Invalid input. Please enter integer values or decamils for grades.")
                continue

            # Write the student's record to the CSV file
            writer.writerow([first_name, last_name, exam1_grade, exam2_grade, exam3_grade])
            print(f"Grades for {first_name} {last_name} have been saved.")

# Run the function to enter student grades

grade = 0

while grade != 'done':
    grade = enter_grades()
