"""
                    Main Objectives
1. Explain Python's basic data types: int, float, and str.
2. Introduce the input() function for interactive programs.
3. Show how to cast data types (int(), float(), str()).
"""


# Introduction to data types: integer (int), floating-point (float), and string (str)
age = 25               # int
height = 5.9           # float
name = "Alice"         # string

# # Displaying types of variables
# print("Age is of type:", type(age))
# print("Height is of type:", type(height))
# print("Name is of type:", type(name))

# Taking input from the user
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))  # Convert input to int
user_height = float(input("What is your height in meters? "))  # Convert input to float

# Displaying user input
print(f"Hello {user_name}, you are {user_age} years old and {user_height} meters tall.")
