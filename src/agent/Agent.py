from model.Board import Board
from model.Directions import Directions
from agent.Move import Move

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
    for i in range(4):
        for j in range(4):
            count += 1 if board.get_tile(i, j) == 0 else 0
    return count



# The score of the move is an average of the scores of the resulting boards
# The score of a board is the max move that can be done on that board



# Every empty space is worth 3 points.
# Every matching pair of adjacent cards is worth 2 points.
# A card next to another card twice its value is worth 2 points.
# A card trapped between two other cards of higher value, or between a wall and a card of higher value, is penalized 5 points.
# Cards of the second-largest size get a bonus of 1 point if they’re next to the largest card, and an extra point if they’re next to a wall.
# Cards of the third-largest size get a bonus of 1 point if they’re next to a wall and are next to a card of the second-largest size.
# The largest card gets a +3 bonus if it’s next to one wall, or a +6 bonus if it’s in a corner.

# https://nbickford.wordpress.com/2014/04/18/how-to-beat-threes-and-2048/