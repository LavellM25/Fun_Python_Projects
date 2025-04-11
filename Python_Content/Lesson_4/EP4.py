# Lesson 4: Control Flow - If Statements and Logical Operators

"""                            Objective:
Teach students how to make decisions in Python using if, elif, and else.
Introduce comparison operators (==, !=, >, <, >=, <=).
Cover logical operators (and, or, not) to combine conditions."""

"""                            Key Concepts:
if, elif, and else (Conditional Statements):
1) Use if to check a condition.
2) Use elif (else if) to check additional conditions.
3) Use else as a fallback if none of the previous conditions are met.

Comparison Operators:
1) ==: Equal to
2) !=: Not equal to
3) >: Greater than
4) <: Less than
5) >=: Greater than or equal to
6) <=: Less than or equal to

Logical Operators:
1) and: True if both conditions are true.
2) or: True if at least one condition is true.
3) not: Negates a condition.
"""

# Control Flow: Making decisions with if, elif, and else

# Asking for user input
age = int(input("Enter your age: "))

# Using if, elif, and else to determine age group
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

# Logical operators: Example with login system
username = input("Enter your username: ").lower()
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Welcome, admin!")
elif username == "admin" and password != "1234":
    print("Incorrect password.")
elif username != "admin" and password == "1234":
    print("Incorrect username.")
else:
    print("Access denied.")
# #
# Using logical operators in a decision
temperature = float(input("Enter the temperature in Fahrenheit: "))
if temperature < 0 or temperature > 35:
    print("Extreme weather alert!")
else:
    print("The weather is normal.")


"""
                        Code Challenge: 
A) Write a program that asks the user for a grade percentage and outputs:
"A" for 90-100%,
"B" for 80-89%,
"C" for 70-79%,
"D" for 60-69%,
"F" for below 60%.

B) Create a login system that only allows access if the 
username is "user123" or "guest" and the password is "pass123".

"""
