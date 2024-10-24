"""
Author: Lavell McGrone
Date: 2024-23-10
Description: Validate and format book titles by correcting capitalization and spacing based on specific title case rule.
"""


def main():
    """
    Main execution control method.
    :return: None
    """
    print("Welcome to the title validation program.")  # Print the introductory statement

    try:
        title = inputs()  # Get the title input from the user and validate it
        corrected_title = process_title(title)  # Process and format the title correctly
        outputs(corrected_title)  # Output the corrected title

        # Loop to ask if the user wants to continue
        while True:
            restart = input("\nWould you like to validate another title? (y/n): ").strip().lower()
            if restart == 'y':  # Restart the loop
                print("\nRestarting the program...\n")
                break
            elif restart == 'n':  # Exit the program
                print("Thanks for using the program!")
                return  # Exit the program
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input
    except Exception as err:
        print(f"An error occurred: {err}")  # Handle any unexpected errors and prompt for restart


def inputs():
    """
    Ask the user for a book title and validate the input.
    :return: A valid, non-blank book title.
    """
    while True:
        title = input("Please enter a title for validation & correction: ").strip()
        if title == "":  # Validate that the title is not blank
            print("Please try again. The title cannot be blank.")
        else:
            return title


def process_title(title):
    """
    Process the book title by correcting capitalization and formatting.
    :param title: The original title input by the user.
    :return: The formatted and corrected title.
    """
    # Split the title into individual words
    words = title.split()

    # Words that should be lowercase unless at the start or end
    lowercase_words = ["the", "a", "an", "of"]

    corrected_title = []
    for i, word in enumerate(words):
        # Capitalize the first and last word regardless
        if i == 0 or i == len(words) - 1:
            corrected_title.append(word.capitalize())
        # Lowercase words like "the", "a", "an", and "of" if they are not first or last
        elif word.lower() in lowercase_words:
            corrected_title.append(word.lower())
        else:
            corrected_title.append(word.capitalize())  # Capitalize all other words

    # Join the words back together to form the corrected title
    return " ".join(corrected_title)


def outputs(corrected_title):
    """
    Display the corrected title.
    :param corrected_title: The formatted title.
    :return: None
    """
    print(f"The corrected title is: {corrected_title}\n")


# Run the program
if __name__ == "__main__":
    main()
