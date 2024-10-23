from model.Board import Board
from model.Directions import Directions
from agent.Move import Move
from agent.helpers import num_blank_spaces, num_combinable_pairs, to_tuple, highest_tile_number;

DEPTH = 4

def expectimax(board: Board, tiles: int):
    return max_move(board, tiles, DEPTH).dir


def max_move(board: Board, tiles:list, depth: int) -> Move:

    bestMove = Move(None, -10)

    for dir in Directions:
        copy = board.copy()
        coords = copy.shift(dir)
        if coords:
            score = expecti_board(copy, tiles, coords, depth-1)
            if score > bestMove.score:
                bestMove = Move(dir, score)

    return bestMove    


def expecti_board(board: Board, tiles: list, coords: list, depth: int) -> Move:

    score = 0

    for i, j in coords:
        for tile in tiles:
            copy = board.copy()
            copy.add_tile(tile, i, j)
            score += max_move(copy, [1, 2, 3], depth).score if depth > 0 else evaluate_board(copy)

    score /= len(coords) * len(tiles)

    return score


def evaluate_board(board: Board):
    if not board.can_shift():
        return 0
    count = 1
    count += 3 * num_blank_spaces(board)
    count += num_combinable_pairs(board)
    return count



# The score of the move is an average of the scores of the resulting boards
# The score of a board is the max move that can be done on that board