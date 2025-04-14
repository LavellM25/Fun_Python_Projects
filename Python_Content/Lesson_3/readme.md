# 🧠 Python Basics: Data Types, Input, and Type Casting

This project introduces some of Python's core programming concepts through a simple interactive script.

## 🎯 Main Objectives
1. Explain Python's basic data types: `int`, `float`, and `str`
2. Introduce the `input()` function for interactive programs
3. Demonstrate how to cast data types using `int()`, `float()`, and `str()`


## 🧾 Code Overview
- This script first defines a few variables using basic data types. Then, it prompts the user to enter their name, age, and height. 
- The script performs type conversions to handle the input properly and displays the final output using formatted strings.


## 🧪 Example Interaction:
- What is your name? Lavell
- How old are you? 27
- What is your height in meters? 1.82
- Hello Lavell, you are 27 years old and 1.82 meters tall.


## ✅ Bonus Challenge
- Add try/except blocks to catch errors from bad input
- Use type() to print and confirm the data type of each input
- Ask for more user info (e.g., favorite color, birthday)
- Format the output into a multi-line summary


### Sample Code:

```python
# Variable examples
age = 25               # Integer
height = 5.9           # Float
name = "Alice"         # String

# User input
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))  # Convert input to int
user_height = float(input("What is your height in meters? "))  # Convert input to float

# Output
print(f"Hello {user_name}, you are {user_age} years old and {user_height} meters tall.")
