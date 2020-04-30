import sys

def initialize_board():
    global N, board
    N = 9
    board = []
    fo = open(sys.argv[1], 'r')
    for _ in range(N):
        board.append(list(map(int, fo.readline().split('  '))))
    fo.close()

    print('\nStarting board:')
    print_board()

def solve(x, y):
    if x >= N and y >= N-1:
        print('Solution:')
        print_board()
        exit()

    if x >= N:
        x = 0
        y += 1

    if board[y][x] != 0:
        solve(x+1, y)
        return False

    for n in range(1, N+1):
        if is_valid(n, x, y):
            # print('valid square found:', n, 'at (', x, ',', y, ')')
            set_square(n, x, y)
            if not solve(x+1, y):
                set_square(0, x, y)

    # print('error! no valid options at (', x, ',', y, ')... returning to previous stack')
    return False

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
    box = [board[y_start+i][x_start+j] for i in range(3) for j in range(3)]
    return n not in row and n not in column and n not in box

def print_board():
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j], '   ', end='')
        print('\n')

def set_square(n, x, y):
    board[y][x] = n

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('\nusage: python solver.py [game_file]\n')
        exit()
    initialize_board()
    solve(0,0)
    print('This game has no valid solution')