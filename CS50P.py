import string

name = input("What's your name? ")
age = int(input("How old are you? ")) 

# use .strip() to remove the white spaces in the input
name = name.strip()

# use .capitalize() to capitalize the first letter of the input
name = name.capitalize()

# use f"" to print the variables{} that are inside the print function
print(f"Hello, {name}")

# use sep="" to separate the variables that are inside the print function
print(name, age, sep=", ")

# use end="" to print the variables in the same line
print(name, end=" ")
print(age)

# edX CS50P IDE - Functions & Variables