"""
    Date: 1-19-2025
    Description: 2048 game with GUI that restarts once user has reached 2048.
"""

import tkinter as tk
import random

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.board = [[0] * 4 for _ in range(4)]
        self.cell_colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
            32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
            512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        self.text_colors = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                            32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                            512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
        self.init_ui()
        self.reset_game()

    def init_ui(self):
        self.frame = tk.Frame(self.window, bg="#bbada0", width=500, height=500)
        self.frame.grid(padx=10, pady=10)
        self.cells = [[None for _ in range(4)] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                cell = tk.Label(self.frame, text="", bg="#cdc1b4",
                                font=("Arial", 24, "bold"), width=4, height=2)
                cell.grid(row=r, column=c, padx=5, pady=5)
                self.cells[r][c] = cell

        self.window.bind("<Key>", self.on_key_press)

    def reset_game(self):
        """Reset the game board."""
        self.board = [[0] * 4 for _ in range(4)]
        self.add_new_number()
        self.add_new_number()
        self.update_ui()

    def add_new_number(self):
        """Add a new number (2 or 4) to a random empty cell."""
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def update_ui(self):
        """Update the UI to reflect the current state of the board."""
        for r in range(4):
            for c in range(4):
                value = self.board[r][c]
                cell = self.cells[r][c]
                cell.config(text=str(value) if value else "",
                            bg=self.cell_colors.get(value, "#cdc1b4"),
                            fg=self.text_colors.get(value, "#f9f6f2"))

    def slide_and_merge(self, row):
        """Slide and merge a single row to the left."""
        non_zero = [num for num in row if num != 0]
        new_row = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_row.append(non_zero[i] * 2)
                skip = True
            else:
                new_row.append(non_zero[i])
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
                if self.board[r][c] == 0:
                    return True
                if c < 3 and self.board[r][c] == self.board[r][c + 1]:
                    return True
                if r < 3 and self.board[r][c] == self.board[r + 1][c]:
                    return True
        return False

    def has_won(self):
        """Check if the player has won."""
        return any(2048 in row for row in self.board)

    def on_key_press(self, event):
        """Handle key press events for movement."""
        key = event.keysym
        previous_board = [row[:] for row in self.board]

        if key == "Up":
            self.move_up()
        elif key == "Down":
            self.move_down()
        elif key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()

        if self.board != previous_board:
            self.add_new_number()
            self.update_ui()

            if self.has_won():
                self.show_message("You Win!")
            elif not self.is_move_possible():
                self.show_message("Game Over!")

    def show_message(self, message):
        """Show a game-over or win message."""
        popup = tk.Toplevel(self.window)
        popup.title("Game Over")
        label = tk.Label(popup, text=message, font=("Arial", 18, "bold"))
        label.pack(pady=20)
        button = tk.Button(popup, text="Restart", command=lambda: [self.reset_game(), popup.destroy()])
        button.pack(pady=10)

    def run(self):
        """Run the main game loop."""
        self.window.mainloop()


if __name__ == "__main__":
    Game2048().run()
