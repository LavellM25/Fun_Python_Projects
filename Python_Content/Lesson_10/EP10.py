"""
Lesson 10:

Introduce list comprehensions to create lists in a concise and readable way.
Explain lambda functions, which allow for quick, one-time use functions.
Show how these concepts make code more efficient and Pythonic.


Key Concepts:
1. What is a List Comprehension?
A list comprehension is a shorter way to create lists.
Instead of using a loop to build a list, you can generate it in a single line.
new_list = [expression for item in iterable if condition]

2. Examples of List Comprehensions:
Creating a list from a range of numbers.
Filtering elements based on a condition.
Performing operations on elements while creating a list.

3. What is a Lambda Function?
A lambda function is an anonymous function (a function without a name).
It's used for simple operations and is often used with map(), filter(), and sort().
lambda arguments: expression

4. Using Lambda Functions:
Performing calculations quickly.
Sorting data based on custom rules.
Filtering elements from a list.
"""

# Using List Comprehensions
print("Using List Comprehensions")

# Creating a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
# Explanation:
# 1. We loop through numbers from 1 to 10 using range(1, 11)
# 2. For each number `x`, we compute `x**2` (square of x)
# 3. We store the squared values in the list `squares`
print("List of squares:", squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
# Explanation:
# 1. We iterate through each number in the list `numbers`
# 2. We check if the number is even using `num % 2 == 0`
# 3. If true, we include it in the `even_numbers` list
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Creating a list of uppercase words
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
# Explanation:
# 1. We iterate through each word in the list `words`
# 2. We convert each word to uppercase using `word.upper()`
# 3. The transformed words are stored in `uppercase_words`
print("Uppercase words:", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']


print("\nUsing Lambda Functions")

# Simple lambda function to multiply a number by 2
double = lambda x: x * 2
# Explanation:
# 1. `lambda x: x * 2` defines an **anonymous function** (lambda function)
# 2. It takes an input `x` and returns `x * 2`
print("Double of 5:", double(5))  # Output: 10


# Using lambda with map() to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# Explanation:
# 1. `map()` applies a function to each item in `numbers`
# 2. The lambda function `lambda x: x**2` squares each number
# 3. `list()` converts the result from `map()` into a list
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]


# Using lambda with filter() to filter out odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# Explanation:
# 1. `filter()` is used to keep only elements that return True for the condition
# 2. The lambda function `lambda x: x % 2 != 0` checks if the number is odd
# 3. `list()` converts the filtered result into a list
print("Odd numbers:", odd_numbers)  # Output: [1, 3, 5]


# Sorting a list of tuples based on the second value using lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
# Explanation:
# 1. `sorted()` sorts a list, and `key` defines **what to sort by**
# 2. The lambda function `lambda student: student[1]` selects the second value (score) for sorting
# 3. `reverse=True` sorts in descending order (highest score first)
print("Sorted students by score:", sorted_students)
# Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

"""
Summary of Key Takeaways
✅ List Comprehensions → A short way to create lists with conditions and transformations.
✅ Lambda Functions → Anonymous functions useful for quick, one-time operations.
✅ map() with lambda → Used to transform elements in a list.
✅ filter() with lambda → Used to filter elements based on conditions.
✅ sorted() with lambda → Used to sort elements based on specific values.
"""


"""
                                Student Challenge: 
1. Write a list comprehension to create a list of cubes (numbers raised to the third power) from 1 to 10.

2. Use a lambda function inside the map() function to convert a list of temperatures in Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    
3. Use a lambda function inside the filter() function to extract words longer than 5 characters from a list of words.
"""