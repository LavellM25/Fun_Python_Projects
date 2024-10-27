"""
Author: Lavell McGrone
Date: 2024-23-10
Description: Collects, validates, and formats feedback phrases ensuring proper capitalization and punctuation.
"""


def main():
    """
    Main function that controls the program flow.
    :return: None
    """
    print("Welcome to the feedback generator.")  # Print the introductory statement

    while True:
        try:
            feedback_input = inputs()  # Get feedback phrases from user
            feedback_list = process_feedback(feedback_input)  # Process and format the feedback phrases
            outputs(feedback_list)  # Output the formatted feedback list

            # Prompt for restart
            while True:
                restart = input("\nWould you like to try again? Enter y or n: ").strip().lower()
                if restart == 'y':  # Restart the program
                    print("\nRestarting the program...\n")
                    break
                    main()
                elif restart == 'n':  # Exit the program
                    print("Thanks for helping us build our feedback library.")
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Handle unexpected errors and allow the program to restart


def inputs():
    """
    Ask the user to enter multiple feedback phrases and validate the input.
    :return: A valid string of feedback phrases.
    """
    # Start a loop that will keep asking for input until it's valid
    while True:
        # Prompt the user to enter feedback phrases and remove any surrounding spaces
        feedback = input("Please enter multiple feedback phrases, each ending in an exclamation point: ").strip()
        if not feedback:    # Check if the input is empty (no text entered)
            # Let the user know the input can't be blank and ask them to try again
            print("The input cannot be blank. Please try again.")
        # Check if there's at least one exclamation point in the input
        elif '!' not in feedback:
            # Inform the user that each phrase needs an exclamation point and prompt to re-enter
            print("Each phrase must end in an exclamation point. Please try again.")
        else:
            return feedback    # If the input from user passes both checks, return it as a valid input


def process_feedback(feedback):
    """
    Process the feedback by cleaning, capitalizing, and adding exclamation points.
    :param feedback: The raw input string from the user.
    :return: A list of corrected feedback phrases.
    """
    # Split the input text by '!' to separate phrases. Strip extra spaces and exclude any empty entries
    raw_phrases = [phrase.strip() for phrase in feedback.split('!') if phrase.strip()]
    corrected_phrases = []   # Create an empty list to store the corrected phrases
    # Loop through each phrase in the list of raw phrases
    for phrase in raw_phrases:
        # Capitalize the first letter, remove extra spaces, and add an exclamation point
        corrected_phrases.append(f"{phrase.capitalize()}!")
    return corrected_phrases    # Return the final list of corrected feedback phrases

# replace phrases that you don't want the user to use check if it isalpha, if not ignore it


def outputs(feedback_list):
    """
    Display the corrected list of feedback phrases.
    :param feedback_list: A list of formatted feedback phrases.
    :return: None
    """
    print("\nHere are your feedback phrases: ")   # print message to the user to introduce the list of feedback phrases
    for idx in range(len(feedback_list)):   # Access each item in feedback_list with feedback_list[idx]
        print(f"{idx + 1}: {feedback_list[idx]}")  # Add 1 to idx so numbering start from 1 instead of 0 for readability
    print()   # Add extra line for spacing purposes


# Run the program
if __name__ == "__main__":
    main()
