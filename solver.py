# Python sudoku solver that takes in a file representing a valid or invalid Sudoku game
# and prints to stdout a valid solution to that game if one exists (no UI yet).

N = 9

def initialize_board():
    global board
    board = []
    file_name = 'game.txt'
    fo = open(file_name, 'r')
    for _ in range(N-1):
        board.append(list(map(int, fo.readline()[:-1].split('  ')))) # ordered by row, e.g. if board[0] is the first square,
                                                                     # board[9] is the first square of the second row
    board.append(list(map(int, fo.readline().split('  ')))) # no newline on last row
    fo.close()

    print_board()

def solve():
    # for x in range(N):
    #     for y in range(N):
    return 0

# assumes n has not been added to the board at (x,y) yet
def is_valid(n, x, y):
    row = board[y]
    column = [board[i][x] for i in range(N)]
    
    if x in range(3):
        x_start = 0
    elif x in range(3,6):
        x_start = 3
    else:
        x_start = 6
    if y in range(3):
        y_start = 0
    elif y in range(3,6):
        y_start = 3
    else:
        y_start = 6
    box = [board[y_start+i][x_start+j] for i in range(0,3) for j in range(0,3)]
    return n not in row and n not in column and n not in box

def print_board():
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j], '   ', end='')
        print('\n')

if __name__ == "__main__":
    initialize_board()
    solve()