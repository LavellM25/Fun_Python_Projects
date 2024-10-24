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
    while True:
        feedback = input("Please enter multiple feedback phrases, each ending in an exclamation point: ").strip()
        if not feedback:
            print("The input cannot be blank. Please try again.")
        elif '!' not in feedback:
            print("Each phrase must end in an exclamation point. Please try again.")
        else:
            return feedback


def process_feedback(feedback):
    """
    Process the feedback by cleaning, capitalizing, and adding exclamation points.
    :param feedback: The raw input string from the user.
    :return: A list of corrected feedback phrases.
    """
    # Split the feedback based on '!' but exclude any empty entries by filtering
    raw_phrases = [phrase.strip() for phrase in feedback.split('!') if phrase.strip()]

    corrected_phrases = []
    for phrase in raw_phrases:
        # Capitalize the first letter, remove extra spaces, and add the exclamation point
        corrected_phrases.append(f"{phrase.capitalize()}!")

    return corrected_phrases


def outputs(feedback_list):
    """
    Display the corrected list of feedback phrases.
    :param feedback_list: A list of formatted feedback phrases.
    :return: None
    """
    print("\nHere are your feedback phrases:")
    for idx, phrase in enumerate(feedback_list, start=1):
        print(f"{idx}: {phrase}")
    print()


# Run the program
if __name__ == "__main__":
    main()
