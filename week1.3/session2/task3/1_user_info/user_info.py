# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = str(input("what's your name"))
age = str(input("what's your age"))
fav_colour = str(input("what's your favourite colour"))

with open("/workspaces/semester-1/week1.3/session2/task3/1_user_info/user_info.txt","w") as x:
    x.write(f"{name}\n{age}\n{fav_colour}")
    
with open("/workspaces/semester-1/week1.3/session2/task3/1_user_info/user_info.txt", "r") as x:
    print(x.read())

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
