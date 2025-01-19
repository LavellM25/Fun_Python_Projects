"""
Lesson 7
                                    Main Objective:
Introduce Python dictionaries as a way to store data in key-value pairs.
Teach how to create, access, update, and manipulate dictionaries.
Cover common dictionary methods and practical use cases.

                                    Key Concepts:
What is a Dictionary?
A dictionary is a collection of key-value pairs, where each key is unique, and values can be of any data type.
Dictionaries are defined using curly braces {}.

Accessing Values:
Use the key to access the corresponding value: dictionary[key].

Adding and Updating Key-Value Pairs:
Add new key-value pairs or update existing ones by assigning values to keys: dictionary[key] = value.

Removing Key-Value Pairs:
Use pop(key) to remove a specific pair, or popitem() to remove the last added pair.

Iterating Through a Dictionary:
Use loops to process keys, values, or both.
"""

# What is a dictionary?
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# print("Original dictionary:", person)

# Accessing values
# print("Name:", person["city"])  # Access value by key
# print("Age:", person["age"])
# #
# Adding and updating key-value pairs
# person["profession"] = "Engineer"  # Adding a new key-value pair
# print("After adding profession:", person)
# person["age"] = 31  # Updating an existing key of age
# print("After updating age:", person)

# # Removing key-value pairs
# removed_value = person.pop("city")  # Remember from lesson 6, .pop() method removes the key "city" and returns value
# #
# # # In this example, will show what value was removed from the city, the last element from dictionary is removed.
# print("Removed city:", removed_value)
# print("After removing city:", person)

# Iterating through a dictionary
# print("\nIterating through dictionary keys:")  # \n make a new line
# for key in person:
#     print(f"Key: {key}, Value: {person[key]}")
#
# print("\nIterating through dictionary items:")
# for key, value in person.items():  # For every key, value in sequence in dictionary, get all key-value pairs
#     print(f"{key}: {value}")  # This will print the key and value of the entire dictionary using a for-loop
# #
# # Using dictionary methods
# print("\nUsing dictionary methods:")
# print("Keys:", person.keys())  # Get all keys
# print("Values:", person.values())  # Get all values
# print("Items:", person.items())  # Get all key-value pairs


"""
                                                Student Challenge: 
Create a dictionary that stores details about your favorite book: title, author, year published, and genre.
    Print the title and author.
    Add a new key for "rating" and assign it a value.
    Remove the genre key from the dictionary.
    
Write a program that takes a list of student names and scores, stores them in a dictionary, and prints:
    The highest score and the student who achieved it.
    The average score.
    
"""
