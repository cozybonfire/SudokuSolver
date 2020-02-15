import os
from tkinter import Tk, Canvas

FOOTER_HEIGHT = 100
SQUARE_SIDE_LENGTH = 60
PADDING = 4
GAME_SIDE_LENGTH = SQUARE_SIDE_LENGTH * 9
WINDOW_WIDTH = GAME_SIDE_LENGTH + PADDING * 2
WINDOW_HEIGHT = GAME_SIDE_LENGTH + FOOTER_HEIGHT

def draw_board():
    for i in range(0, 11):
        y = SQUARE_SIDE_LENGTH * i + PADDING
        border = i % 3 == 0 or i == 10
        if border:
            board.create_line(PADDING, y, GAME_SIDE_LENGTH + PADDING, y, width=3)
        else:
            board.create_line(PADDING, y, GAME_SIDE_LENGTH + PADDING, y)
    for i in range(0, 11):
        x = SQUARE_SIDE_LENGTH * i + PADDING
        border = i % 3 == 0 or i == 10
        if border:
            board.create_line(x, PADDING, x, GAME_SIDE_LENGTH + PADDING, width=3)
        else:
            board.create_line(x, PADDING, x, GAME_SIDE_LENGTH + PADDING)

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

