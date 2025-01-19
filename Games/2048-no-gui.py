"""
    Date: 1-19-2025
    Description: 2048 game with no GUI.
"""

import random
import os

def initialize_game():
    """Initialize the game board."""
    board = [[0] * 4 for _ in range(4)]
    add_new_number(board)
    add_new_number(board)
    return board

def print_board(board):
    """Print the game board."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("2048 Game\n")
    for row in board:
        print(" | ".join(f"{num or ' ':^5}" for num in row))
        print("-" * 21)

def add_new_number(board):
    """Add a new number (2 or 4) to the board at a random empty position."""
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def slide_and_merge(row):
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

def move_left(board):
    """Move all rows to the left."""
    for r in range(4):
        board[r] = slide_and_merge(board[r])

def move_right(board):
    """Move all rows to the right."""
    for r in range(4):
        board[r] = slide_and_merge(board[r][::-1])[::-1]

def move_up(board):
    """Move all columns up."""
    for c in range(4):
        col = slide_and_merge([board[r][c] for r in range(4)])
        for r in range(4):
            board[r][c] = col[r]

def move_down(board):
    """Move all columns down."""
    for c in range(4):
        col = slide_and_merge([board[r][c] for r in range(4)][::-1])[::-1]
        for r in range(4):
            board[r][c] = col[r]

def is_move_possible(board):
    """Check if any moves are possible."""
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return True
            if c < 3 and board[r][c] == board[r][c + 1]:
                return True
            if r < 3 and board[r][c] == board[r + 1][c]:
                return True
    return False

def has_won(board):
    """Check if the player has won the game."""
    return any(2048 in row for row in board)

def game_loop():
    """Main game loop."""
    board = initialize_game()
    while True:
        print_board(board)
        if has_won(board):
            print("Congratulations! You've won the game!")
            break
        if not is_move_possible(board):
            print("Game over! No moves left.")
            break

        move = input("Enter move (W/A/S/D): ").strip().upper()
        if move not in "WASD":
            print("Invalid input. Use W (up), A (left), S (down), D (right).")
            continue

        previous_board = [row[:] for row in board]

        if move == "W":
            move_up(board)
        elif move == "A":
            move_left(board)
        elif move == "S":
            move_down(board)
        elif move == "D":
            move_right(board)

        if board != previous_board:
            add_new_number(board)

if __name__ == "__main__":
    game_loop()
