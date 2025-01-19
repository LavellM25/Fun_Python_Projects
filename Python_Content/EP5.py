"""
                                    Main Objective:
Lesson 5: Loops - for and while
Be able to use loops to automate repetitive tasks using for and while loops, by implementing controlled iterations
with "break" and "continue"
Teach the difference between for loops and while loops.
Demonstrate practical applications of loops such as iterating through lists, ranges, and user-defined conditions.
Introduce break and continue for loop control.
"""

"""
for Loops:
Used to iterate over a sequence (e.g., list, string, range). Syntax: for item in sequence: # Do something

while Loops:
Repeats as long as a condition is True.  Syntax: while condition: # Do something

break and continue:
break: Exits the loop immediately.
continue: Skips the rest of the current iteration and moves to the next.

"""

# # Example of a for loop: Iterating through a range of numbers
# print("Counting from 1 to 25:")
#
# # "Here, we're using a for loop to iterate through a range of numbers from 1 to 5.
# # The range() function generates numbers starting from 1 up to, but not including, 6."
# for i in range(1, 26):  # range(start, stop)
#     print(i)  # "For each number in the range, we print it to the console."

# # Example of a while loop: Guessing game
# print("\nGuess the number game!")
#
# # "Now, let's create a simple guessing game.
# # We define a secret number that the user has to guess."
# secret_number = 7
# guess = 0  # "We initialize the guess variable to 0, so the loop starts."
#
# # "We use a while loop to keep asking the user for their guess until they guess the correct number."
# while guess != secret_number:
#     guess = int(input("Enter your guess (1-10): "))  # "We prompt the user to enter their guess."
#     if guess < secret_number:
#         print("Too low!")  # "If the guess is less than the secret number, we let them know it's too low."
#     elif guess > secret_number:
#         print("Too high!")  # "If the guess is greater than the secret number, we let them know it's too high."
#     else:
#         print("Correct! You guessed it!")  # "If the guess is correct, we congratulate the user and exit the loop."

# "Now, let's demonstrate the use of break and continue in a loop."

# print("Demonstrating 'break' and 'continue':")
#
# # Using a loop to search for a number
# for num in range(1, 11):  # Loop through numbers 1 to 10
#     if num == 5:
#         print("Found the number 5! Breaking the loop.")  # Stop the loop when number is 5
#         break  # Exit the loop completely
#     print(f"Checking number: {num}")  # Show the numbers being checked


# Using a loop to skip even numbers using "continue"
for num in range(1, 11):  # Loop through numbers 1 to 10
    if num % 2 == 0:  # Check if the number is even
        continue  # Skip this iteration for even numbers
    print(f"Odd number: {num}")  # Show only the odd numbers



"""
                                            Student Challenge: 
1. Write a for loop that prints the multiplication table (1 to 10) for a number provided by the user.
2. Create a while loop that keeps asking the user for input until they type "exit".
3. Write a program using a loop that calculates the sum of all numbers from 1 to a user-defined value.
"""

