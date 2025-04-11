"""
Lesson 6
                                    Main Objective:
Introduce Python lists as a way to store multiple items in a single variable.
Teach how to access, modify, and manipulate list elements.
Cover basic list operations like appending, removing, slicing, and looping through lists.
"""

"""                                 
                                    Key Objective: 
What is a List?
    A list is a collection of items (elements) that can hold different data types.
    Lists are defined using square brackets [].                                 

Accessing Elements:
    Use indexing to access individual elements (starting from 0).
    Negative indexing allows access from the end of the list.

Basic List Operations:
    Adding items: append(), insert().
    Removing items: remove(), pop().
    Slicing: Extracting parts of a list using [start:stop:step].
    
Iterating Through Lists:
    Use for loops to process each item in a list.
"""



# What is a list?
fruits = ["apple", "banana", "cherry", "grape", "blueberry", "mango", "orange"]
# print("Original list:", fruits)  # Display the list
# print(fruits)  # to display the entire list


# # Accessing elements
# print("First fruit:", fruits[0])  # Access the first element
#
# # For indexing purposes -1 will get the last element from the list
# # will count backwards starting with -1
# print("Last fruit:", fruits[-1])  # Access the last element.
# #
# # Modifying the list
# fruits[1] = "blueberry"  # Change "banana" to "blueberry"
# print("Modified list:", fruits)  # Modified list after switching banana for blueberry
#
# # Adding items to the list
# fruits.append("strawberry")  # Add a new item to the end
# print("After appending:", fruits)  # the .append() method adds items to the end of the list.
# # To add items in a specific order, use fruits[index] = new variable to add item in specific order.

# fruits.insert(2, "fig")  # Insert "fig" at index 2
# print("After inserting:", fruits)  # you can use the .insert() method to insert a particular element in the list.


# # Removing items from the list
# fruits.remove("apple")  # Remove "cherry"
# print("After removing 'cherry':", fruits)  # .remove() method allows you to remove a certain element in the list.
# print(fruits[2])

# popped_fruit = fruits.pop()  # Remove the last item and save it
# print("After popping:", fruits)  # the .pop() method deletes the last element in the list.
# print("Popped fruit:", popped_fruit)

# Slicing the list
#
# # Example 1: Getting the first two items
# print("First two fruits:", fruits[:2])
# # "What does this mean?"
# # When you write fruits[:2], you're slicing the list to get a portion of it.
# # The `:2` tells Python to start from the beginning of the list (default)
# # and stop at index 2, but NOT including the item at index 2.
# # In Python, the stop index in slicing is exclusive, so you only get elements 0 and 1.
#
# # Example 2: Getting every other item
# print("Every other fruit:", fruits[::3])
# # "What does this mean?"
# # When you write fruits[::2], you're telling Python to get all elements in the list
# # but to step by 2 (skip every second item).
# # The first `:` means "start at the beginning," the second `:` means "go to the end,"
# # and the `2` means "step by 2."
# # This is useful when you want to filter out alternate items or process items at intervals.

# Quick analogy for beginners:
# Think of slicing like taking a piece out of a cake (the list).
# The numbers `[start:stop: interval that you wish to count by]` tell Python:
# - Start where you want to cut (start),
# - Stop where you want the slice to end (stop, not including that point),
# - Step by how many slices to skip (step).

#
# # Iterating through the list
# print("Fruits in the list:")
# for fruit in fruits:   # Ep.5 Syntax: for item in sequence: # Do something
#     print(fruit)


"""
                                                Student Challenge: 
Create a list of your five favorite movies.
    Print the first and last movie using indexing.
    Add a new movie to the list and remove one you don't like anymore.
    
Write a program that takes five numbers as input, stores them in a list, and calculates:
    The sum of the numbers.
    The average of the numbers.
"""
