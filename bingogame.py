import random

def main():
    # Generate the player's bingo card
    player_card = generate_card()
    print("Your Bingo Card:")
    display_card(player_card)

    # Start the game
    print("\nLet's play Bingo!")
    numbers_called = []
    while True:
        input("Press Enter to draw a number...")
        number = draw_number(numbers_called)
        print(f"Number drawn: {number}")
        numbers_called.append(number)

        # Mark the number on the player's card
        mark_card(player_card, number)
        display_card(player_card)

        # Check for Bingo
        if check_bingo(player_card):
            print("Bingo! You win!")
            break

        # Allow the player to quit
        if input("Type 'quit' to exit or press Enter to continue: ").lower() == 'quit':
            print("Thanks for playing!")
            break

# Generate a Bingo card with random numbers
def generate_card():
    card = {}
    columns = {
        "B": range(1, 16),
        "I": range(16, 31),
        "N": range(31, 46),
        "G": range(46, 61),
        "O": range(61, 76)
    }
    for column, numbers in columns.items():
        card[column] = random.sample(numbers, 5)
    # The center of the card is a free space
    card["N"][2] = "FREE"
    return card

# Display the Bingo card with aligned numbers
def display_card(card):
    print("\nB\t\t\tI\t\t\tN\t\t\tG\t\t\tO")
    print("-" * 60)
    for row in range(5):
        for column in "BINGO":
            value = card[column][row]
            print(f"{str(value):<8}", end="\t")
        print()
        print("-" * 60)

# Draw a random number not already called
def draw_number(called_numbers):
    while True:
        number = random.randint(1, 75)
        if number not in called_numbers:
            return number

# Mark the drawn number on the card
def mark_card(card, number):
    for column, numbers in card.items():
        for i in range(len(numbers)):
            if numbers[i] == number:
                card[column][i] = "X"

# Check for Bingo
def check_bingo(card):
    # Check rows
    for row in range(5):
        if all(card[column][row] == "X" or card[column][row] == "FREE" for column in "BINGO"):
            return True
    # Check columns
    for column in "BINGO":
        if all(number == "X" or number == "FREE" for number in card[column]):
            return True
    # Check diagonals
    if all(card[column][i] == "X" or card[column][i] == "FREE" for i, column in enumerate("BINGO")):
        return True
    if all(card[column][4 - i] == "X" or card[column][4 - i] == "FREE" for i, column in enumerate("BINGO")):
        return True
    return False

if __name__ == "__main__":
    main()
