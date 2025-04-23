# MIPO Structure
# Main
def main():
    numbers = get_valid_numbers(5)
    total = sum(numbers)
    average = total / len(numbers)
    show_results(numbers, total, average)

# Input
def get_valid_numbers(count):
    number_list = []
    while len(number_list) < count:
        try:
            user_input = input(f"Enter number {len(number_list) + 1}: ")
            number = float(user_input)  # Accepting floats and integers
            number_list.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return number_list

# Output
def show_results(numbers, total, average):
    print("\nNumbers entered:", numbers)
    print("Total:", total)
    print("Average:", round(average, 2))

# Run the program
main()
