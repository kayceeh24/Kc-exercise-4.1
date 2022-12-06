# Programmer: KC
# Helped By: 

# Function for validates a percent grade depends on the users entered and then prints the level grade
while True:
    grade = input("Enter a percent grade: ")
    grade  = int(grade)
    
    if grade < 0:
        print("Invalid grade! Try again.")
    elif grade <= 49:
        print("")
        print(f"{grade}% is R")
        break
    elif grade <= 59:
        print("")
        print(f"{grade}% is Level 1")
        break
    elif grade <= 69:
        print("")
        print(f"{grade}% is Level 2")
        break
    elif grade <= 79:
        print("")
        print(f"{grade}% is Level 3")
        break
    elif grade <= 100:
        print("")
        print(f"{grade}% is Level 4")
        break
    else:
        print("Invalid grade! Try again.")
