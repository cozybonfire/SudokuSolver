import os
from tkinter import *

FOOTER_HEIGHT = 100
SQUARE_SIDE_LENGTH = 60
BORDER_WIDTH = 3
PADDING = 4
GAME_SIDE_LENGTH = SQUARE_SIDE_LENGTH * 9
WINDOW_WIDTH = GAME_SIDE_LENGTH + PADDING * 2
WINDOW_HEIGHT = GAME_SIDE_LENGTH + FOOTER_HEIGHT

BUTTON_SIDE_LENGTH = 55

def draw_board():
    image = PhotoImage(file=r"")
    for i in range(0,9):
        for j in range(0,9):
            Button(board, image=image, width=BUTTON_SIDE_LENGTH, height=BUTTON_SIDE_LENGTH).grid(row=i, column=j, padx=0, pady=0)
    board.create_rectangle(PADDING, PADDING, GAME_SIDE_LENGTH + PADDING, GAME_SIDE_LENGTH + PADDING, outline="#000", width=BORDER_WIDTH)

    # for i in range(0, 11):
    #     y = SQUARE_SIDE_LENGTH * i + PADDING
    #     border = i % 3 == 0 or i == 10
    #     if border:
    #         board.create_line(PADDING, y, GAME_SIDE_LENGTH + PADDING, y, width=BORDER_WIDTH)
    #     else:
    #         board.create_line(PADDING, y, GAME_SIDE_LENGTH + PADDING, y)
    # for i in range(0, 11):
    #     x = SQUARE_SIDE_LENGTH * i + PADDING
    #     border = i % 3 == 0 or i == 10
    #     if border:
    #         board.create_line(x, PADDING, x, GAME_SIDE_LENGTH + PADDING, width=BORDER_WIDTH)
    #     else:
    #         board.create_line(x, PADDING, x, GAME_SIDE_LENGTH + PADDING)

root = Tk()
root.title('Sudoku Solver')
path = os.path.dirname(os.path.realpath(__file__))
root.iconbitmap(f'{path}/img/favicon.ico')
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')


board = Canvas(root, width=GAME_SIDE_LENGTH+PADDING*2, height=GAME_SIDE_LENGTH+PADDING*2, bg='LIGHTGRAY')
board.pack()

draw_board()

footer = Canvas(root, width=GAME_SIDE_LENGTH, height=FOOTER_HEIGHT, bg='DARKGRAY')
footer.pack()

root.mainloop()

