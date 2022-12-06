# Programmer: KC
# Helped By: 

# Function for validates a percent grade depends on the users entered and then prints the level grade
percent_grade = int(input("Enter a percent grade: "))
while percent_grade < 0 or percent_grade > 100:
    print("Invalid grade! Try again.")
    grade_percent = int(input("Enter a percent grade: "))
if percent_grade < 50:
    print(f"{percent_grade}% is Level R")
elif percent_grade > 49 and percent_grade < 60:
    print(f"{percent_grade}% is Level 1")
elif percent_grade > 59 and percent_grade < 70:
    print(f"{percent_grade}% is Level 2")
elif percent_grade > 69 and percent_grade < 80:
    print(f"{percent_grade}% is Level 3")
elif percent_grade > 79 and percent_grade < 101:
    print(f"{percent_grade}% is Level 4")