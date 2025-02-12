"""
    Date: 1-26-2025
    Description: 2048 game with GUI that will run forever until the user is out of moves.
"""

import tkinter as tk  # Used for creating the graphical interface
import random         # Used to randomly add new numbers (2 or 4) to the grid

class Game2048:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title(f"2048 | Score: 0")  # Initial window title with score

        # Initialize the game board as a 4x4 grid filled with zeros
        self.board = [[0] * 4 for _ in range(4)]

        # Define colors for cells based on their value
        self.cell_colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
            32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
            512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }

        # Define text colors for cells
        self.text_colors = {
            2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
            32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
            512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
        }

        # Initialize the score
        self.score = 0

        # Flag to track if the user continues after reaching 2048
        self.continue_after_win = False

        # Set up the user interface (UI)
        self.init_ui()

        # Start a new game by resetting the game board
        self.reset_game()

    def init_ui(self):
        """Initialize the graphical user interface."""
        # Create a frame to hold the grid of cells
        self.frame = tk.Frame(self.window, bg="#bbada0", width=700, height=700)
        self.frame.grid(padx=10, pady=10)

        # Create a 4x4 grid of cells (labels) within the frame
        self.cells = [[None for _ in range(4)] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                # Create a label for each cell
                cell = tk.Label(self.frame, text="", bg="#cdc1b4",
                                font=("Arial", 36, "bold"), width=6, height=3)
                cell.grid(row=r, column=c, padx=6, pady=6)  # Position the cell in the grid
                self.cells[r][c] = cell  # Store the label in the cells array

        # Bind keyboard events to handle user input (e.g., arrow keys)
        self.window.bind("<Key>", self.on_key_press)

    def reset_game(self):
        """Reset the game board to start a new game."""
        self.board = [[0] * 4 for _ in range(4)]  # Reset the board to all zeros
        self.score = 0  # Reset the score
        self.add_new_number()  # Add the first random number
        self.add_new_number()  # Add the second random number
        self.continue_after_win = False  # Reset the win continuation flag
        self.update_ui()       # Update the graphical display to reflect the board state

    def add_new_number(self):
        """Add a new number (2 or 4) to a random empty cell."""
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0]
        if empty_cells:  # If there are empty cells
            r, c = random.choice(empty_cells)  # Choose a random empty cell
            self.board[r][c] = 2 if random.random() < 0.9 else 4  # 90% chance for 2, 10% for 4

    def update_ui(self):
        """Update the graphical display to reflect the current state of the board."""
        for r in range(4):
            for c in range(4):
                value = self.board[r][c]  # Get the value of the cell
                cell = self.cells[r][c]  # Get the corresponding label
                # Update the label text, background color, and text color
                cell.config(text=str(value) if value else "",
                            bg=self.cell_colors.get(value, "#cdc1b4"),
                            fg=self.text_colors.get(value, "#f9f6f2"))
        # Update the score in the window title
        self.window.title(f"2048 | Score: {self.score}")

    def slide_and_merge(self, row):
        """Slide and merge a single row to the left, updating the score."""
        non_zero = [num for num in row if num != 0]  # Remove all zeros from the row
        new_row = []
        skip = False
        for i in range(len(non_zero)):
            if skip:  # Skip merging the next tile if a merge just happened
                skip = False
                continue
            # If two adjacent tiles are the same, merge them
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged_value = non_zero[i] * 2  # Merge tiles
                new_row.append(merged_value)
                self.score += merged_value  # Update score
                skip = True  # Skip the next tile
            else:
                new_row.append(non_zero[i])  # Add the current tile to the new row
        # Fill the rest of the row with zeros
        return new_row + [0] * (4 - len(new_row))

    def move_left(self):
        """Move all rows to the left."""
        for r in range(4):
            self.board[r] = self.slide_and_merge(self.board[r])

    def move_right(self):
        """Move all rows to the right."""
        for r in range(4):
            self.board[r] = self.slide_and_merge(self.board[r][::-1])[::-1]

    def move_up(self):
        """Move all columns up."""
        for c in range(4):
            col = self.slide_and_merge([self.board[r][c] for r in range(4)])
            for r in range(4):
                self.board[r][c] = col[r]

    def move_down(self):
        """Move all columns down."""
        for c in range(4):
            col = self.slide_and_merge([self.board[r][c] for r in range(4)][::-1])[::-1]
            for r in range(4):
                self.board[r][c] = col[r]

    def is_move_possible(self):
        """Check if any moves are possible."""
        for r in range(4):
            for c in range(4):
                if self.board[r][c] == 0:  # Empty cell exists
                    return True
                if c < 3 and self.board[r][c] == self.board[r][c + 1]:  # Horizontal merge possible
                    return True
                if r < 3 and self.board[r][c] == self.board[r + 1][c]:  # Vertical merge possible
                    return True
        return False

    def has_won(self):
        """Check if the player has reached 2048."""
        return any(2048 in row for row in self.board)

    def on_key_press(self, event):
        """Handle key press events for movement."""
        key = event.keysym  # Get the key pressed by the user
        previous_board = [row[:] for row in self.board]  # Copy the board before making a move

        if key == "Up":
            self.move_up()
        elif key == "Down":
            self.move_down()
        elif key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()

        if self.board != previous_board:  # Only add a new number if the board changed
            self.add_new_number()
            self.update_ui()

            if self.has_won() and not self.continue_after_win:  # Check if the player has won
                self.prompt_continue()  # Ask if they want to continue
            elif not self.is_move_possible():  # Check if no moves are possible
                self.show_message("Game Over!")

    def prompt_continue(self):
        """Prompt the player to continue after winning."""
        popup = tk.Toplevel(self.window)
        popup.title("You Win!")
        label = tk.Label(popup, text="Congratulations! You reached 2048!\nDo you want to continue?",
                         font=("Arial", 16, "bold"))
        label.pack(pady=20)

        # Buttons for "Yes" and "No"
        yes_button = tk.Button(popup, text="Yes", command=lambda: [self.set_continue(True), popup.destroy()])
        no_button = tk.Button(popup, text="No", command=lambda: [self.reset_game(), popup.destroy()])
        yes_button.pack(side="left", padx=20, pady=10)
        no_button.pack(side="right", padx=20, pady=10)

    def set_continue(self, choice):
        """Set the flag to continue the game."""
        self.continue_after_win = choice

    def show_message(self, message):
        """Show a popup message for win or loss."""
        popup = tk.Toplevel(self.window)
        popup.title("Game Over")
        label = tk.Label(popup, text=message, font=("Arial", 18, "bold"))
        label.pack(pady=20)
        button = tk.Button(popup, text="Restart", command=lambda: [self.reset_game(), popup.destroy()])
        button.pack(pady=10)

    def run(self):
        """Run the main game loop."""
        self.window.mainloop()


# Run the game
if __name__ == "__main__":
    Game2048().run()
