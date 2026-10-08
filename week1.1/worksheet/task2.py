"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try:
    amount_saved_monthly=int(input("How much money would you like to save every month?"))
except:
    print("Invalid Amount")
    exit()


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

amount_saved_yearly=amount_saved_monthly*12
print(f"You will save {amount_saved_yearly} every year")

amount_saved_with_interest=amount_saved_yearly*0.008+amount_saved_yearly
print(f"You will save £{amount_saved_with_interest} (with interest) by the end of the year")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

