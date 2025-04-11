"""
Lesson 8
                                            Main Objective:
Introduce Python functions to organize and reuse code effectively.
Teach how to define and call functions.
Explain parameters, arguments, and return values.
Cover the concept of default parameters and keyword arguments.

                                        Key Objectives:
What is a Function?
    A function is a block of reusable code that performs a specific task.
    Functions help make your code cleaner, more modular, and easier to debug.

Defining a Function:
    Use the def keyword to define a function.
    Syntax:
    def function_name(parameters):
        # Code to execute

Calling a Function:
    Use the function name followed by parentheses: function_name(arguments).

Parameters and Arguments:
    Parameters are placeholders in the function definition.
    Arguments are the values passed to the function when called.

Return Values:
    Use the return statement to send data back from the function.

Default Parameters:
    Set default values for parameters to make them optional.

Keyword Arguments:
    Pass arguments using the parameter name for clarity.

"""

# Defining and calling a basic function
# def greet():
#     print("Happy Birthday Steve")
#     print("Happy Birthday Steve")
#     print("Happy Birthday Steve")
#     print("Happy Birthday Steve")
#     print("Happy Birthday Steve")
#
# greet()  # Calling the function

# Function with parameters
# def greet_user(name):
#     print(f"Hello, {name}! Great to see you.")
#
# greet_user("Alice")  # Calling with an argument

# # Function with parameters and return values
# def add_numbers(a, b):
#     return a + b
#
# result = add_numbers(10, 5)
# print(f"The sum is: {result}")
#
# # Function with default parameters
# def describe_pet(pet_name, animal_type="dog"):
#     print(f"I have a {animal_type} named {pet_name}.")
#
# describe_pet("Buddy")  # Uses default value for animal_type
# describe_pet("Mittens", "cat")  # Overrides the default value

# Function with keyword arguments
def calculate_area(length, width):
    return length * width
#
area = calculate_area(width=5, length=10)  # Keyword arguments
print(f"The area is: {area}")


"""
                                        Student Challenge: 
Write a function that takes two numbers as input and returns their product.
    Call the function with different numbers and print the results.

Create a function that takes a person's name and age, and prints a message like:
    "John is 25 years old."
    Allow the age parameter to have a default value of 18.

Write a function to calculate the area of a circle.
    Use a default value for π (e.g., 3.14) and allow the user to specify it if needed.
"""
