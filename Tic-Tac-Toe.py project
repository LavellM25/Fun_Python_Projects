from tkinter import *
import random

def next_turn(row_index, column_index):

    global player

    if buttons[row_index][column_index]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row_index][column_index]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row_index][column_index]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():

    for row_index in range(3):
        if buttons[row_index][0]['text'] == buttons[row_index][1]['text'] == buttons[row_index][2]['text'] != "":
            buttons[row_index][0].config(bg="green")
            buttons[row_index][1].config(bg="green")
            buttons[row_index][2].config(bg="green")
            return True

    for column_index in range(3):
        if buttons[0][column_index]['text'] == buttons[1][column_index]['text'] == buttons[2][column_index]['text'] != "":
            buttons[0][column_index].config(bg="green")
            buttons[1][column_index].config(bg="green")
            buttons[2][column_index].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row_index in range(3):
            for column_index in range(3):
                buttons[row_index][column_index].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row_index in range(3):
        for column_index in range(3):
            if buttons[row_index][column_index]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row_index in range(3):
        for column_index in range(3):
            buttons[row_index][column_index].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('times new roman', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('times new roman', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row_index in range(3):
    for column_index in range(3):
        buttons[row_index][column_index] = Button(frame, text="", font=('times new roman', 40), width=5, height=2,
                                                  command=lambda row=row_index, column=column_index: next_turn(row, column))
        buttons[row_index][column_index].grid(row=row_index, column=column_index)

window.mainloop()
