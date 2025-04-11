"""
Lesson 9
                                            Main Objective
Introduce tuples and sets, two important data structures in Python.
Explain the key differences between tuples and lists.
Teach how sets work and how they help with unique values and fast lookups.
Cover basic operations for tuples and sets, including indexing, adding/removing elements, and performing set operations.


                                        Key Concepts
1. What is a Tuple?
    A tuple is an immutable ordered collection of elements.
    Unlike lists, tuples cannot be modified after creation.
    Tuples are defined using parentheses ().

2. Working with Tuples:
    Accessing elements using indexing (tuple[index]).
    Slicing tuples (tuple[start:stop]).
    Tuple packing and unpacking.
    Common tuple methods (count(), index()).

3. What is a Set?
    A set is an unordered collection of unique elements.
    Defined using curly braces {} or the set() function.
    No duplicates are allowed in a set.
    Useful for fast lookups and removing duplicate values.

4. Working with Sets:
    Adding and removing elements (add(), remove(), discard()).
    Set operations (union(), intersection(), difference()).
    Checking membership (in keyword).
"""

# Tuples in Python
# print("Working with Tuples")
#
# # Creating a tuple
# colors = ("red", "green", "blue", "yellow", "orange", "purple", "black")
# print("Original tuple:", colors)

# Accessing tuple elements
# print("First color:", colors[0])  # Indexing
# print("Last color:", colors[-1])  # Negative indexing

# Indexing, if you try to retrieve an item that is out of position, you will receive an error
# print("color:", colors[7])

# Slicing tuples
# print("First two colors:", colors[:2]) # Extracts elements from index 0 up to, but NOT including, index 2.

# print(colors[1:])  # Output: If you wanted to include all elements from index 1 onward.
# print(colors[1:5]) # output is index 1 until index 4, not including 5

"""
sequence[start:stop]
start (optional) → The index where slicing begins. If omitted, it defaults to 0 (the first element).
stop → The index where slicing stops. It does not include the element at this index (stop is exclusive).
step (optional) → Specifies the interval (default is 1).
"""

# Tuple unpacking
# rgb_values = ("r", "g", "b")
#
# print(f"Unpacked rgb_values: {0}, {1}, {2}")  # get the element by position
#
# Tuple methods
# print("Index of 'green':", colors.index("green"))
# print("Count of 'blue':", colors.count("blue"))

# Immutable property of tuples (This will cause an error if uncommented)
# colors[0] = "yellow"
#
# print("\nWorking with Sets")

# Creating a set
# unique_numbers = {1, 2, 3, 4, 5, 5, 5}  # Duplicate 5s will be removed automatically
# print("Original set:", unique_numbers)
#
# # Adding and removing elements
# unique_numbers.add(6)
# unique_numbers.remove(2)  # Removes 2
# print("Updated set:", unique_numbers)
# print("Set after 2 was removed", unique_numbers)
#
# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# print("Union of sets:", set_a | set_b)  # Combines both sets
# print("Intersection of sets:", set_a & set_b)  # Common elements
# print("Difference (A - B):", set_a - set_b)  # Elements only in set_a that is not the same as set b
# print("Difference (B - A):", set_b - set_a)  # Elements only in set_b that is not the same as set a

# # # Checking membership
print("Is 3 in set_a?", 3 in set_a)   # Will return a boolean value: true or false, in this case, it is true
print("Is 10 in set_b?", 10 in set_b)   # Will return a boolean value: true or false, in this case, it is false



"""
                                            Student Challenge: 
Create a tuple with five different fruits.
    Print the first and last fruit using indexing.
    Use tuple unpacking to store them into separate variables and print them.

Create two sets:
    One for your favorite foods.
    One for your friend’s favorite foods.
    Print the common favorite foods (intersection).
    Print the unique favorite foods from both sets (union).
"""
