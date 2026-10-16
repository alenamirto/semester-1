# Worksheet 1.2: Task 1 Solution
import sys
continueprogram = True

while continueprogram:
    try:
        grade = int(input("Enter your grade:"))
        result=""
        if grade >=0 and grade <=39:
            result="Fail"
        elif grade >=40 and grade <=69:
            result="Pass"
        elif grade >=70 and grade <=100:
            result="Distinction"
        else:
            sys.exit("Error: Grade must be an integer between 0 and 100")
        print(f"{grade} is a {result}")

    except:
        sys.exit("Error: Grade must be an integer between 0 and 100")

    y_or_n=str(input("continue? y or n:"))
    while y_or_n != "y" and y_or_n !="n":
        y_or_n=str(input("continue? pls enter y or n:"))

    if y_or_n == "y":
        continueprogram=True
    elif y_or_n == "n":
        continueprogram=False



