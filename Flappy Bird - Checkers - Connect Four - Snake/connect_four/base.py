import numpy as np

BLACK = (122, 122, 202)
BLUE = (57, 4, 96)
RED = (200, 0, 0)
YELLOW = (207, 214, 10)

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
NUM_MOVES = ROW_COUNT * COLUMN_COUNT

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4
INF = 100000000000000

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    """Drops a **piece** :)"""
    board[row][col] = piece


def is_valid_location(board, col):
    """Checks for validity of the location clicked by the player"""
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col + 1] == piece\
                and board[row][col + 2] == piece and board[row][col + 3] == piece:
                return True

    # Check vertical locations for win
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row + 1][col] == piece\
                and board[row + 2][col] == piece and board[row + 3][col] == piece:
                return True

    # Check positively sloped diaganols
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][col] == piece and board[row + 1][col + 1] == piece\
                    and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row - 1][col + 1] == piece\
                    and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                return True
