# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
#outputs original string
print(f"Modified String 1: {user_string.lower()}")
#outputs string in all lowercase
print(f"Modified String 2: {user_string.upper()}")
#outputs string in all uppercase
print(f"Modified String 3: {user_string.strip()}")
#outputs string without trailing and leading whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}")
#replaces 'a' chars in the string with @
print(f"Modified String 5: {user_string.capitalize()}")
#capitalises first character
print(f"Modified String 6: {user_string[::-1]}")
#reverses string order
print(f"Modified String 7: {user_string.title()}")
#titlecases the string
print(f"Modified String 8: {len(user_string)}")
#length of string
print(f"Modified String 9: {user_string.find('a')}")
#finds first occurnece of a
print(f"Modified String 10: {user_string.count('a')}")
#counts how many 'a's
print(f"Modified String 11: {user_string.startswith('Hello')}")
#checks if string starts with hello
print(f"Modified String 12: {user_string.endswith('!')}")
#checks if string ends with '!'
print(f"Modified String 13: {user_string.isalnum()}")
#checks if string is alphanumeric string
print(f"Modified String 14: {user_string.isalpha()}")
#checks if string is alphabetic string
print(f"Modified String 15: {user_string.isdigit()}")
#checks if string is digit string



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!