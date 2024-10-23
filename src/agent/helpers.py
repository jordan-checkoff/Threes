from model.Board import Board
from model.helpers import can_combine

def num_blank_spaces(board: Board) -> int:
    count = 0
    for i in range(4):
        for j in range(4):
            count += 1 if board.get_tile(i, j) == 0 else 0

    return count


def num_combinable_pairs(board: Board) -> int:
    count = 0
    for i in range(3):
        for j in range(3):
            tile = board.get_tile(i, j)
            if tile == 0:
                continue
            count += 1 if can_combine(tile, board.get_tile(i+1, j)) else 0
            count += 1 if can_combine(tile, board.get_tile(i, j+1)) else 0

    return count


def to_tuple(board: Board) -> tuple:
    row1 = tuple(board.board[0])
    row2 = tuple(board.board[1])
    row3 = tuple(board.board[2])
    row4 = tuple(board.board[3])
    return (row1, row2, row3, row4)

def highest_tile_number(board):
    tiles = [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]

    highest_tile = max(max(board.board[0]), max(board.board[1]), max(board.board[2]), max(board.board[3]))

    return tiles.index(highest_tile)