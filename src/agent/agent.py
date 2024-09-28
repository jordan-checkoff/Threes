from model.Model import Model

DEPTH = 4


options = [
    lambda x: x.shift_up(),
    lambda x: x.shift_right(),
    lambda x: x.shift_down(),
    lambda x: x.shift_left(),
]

def choose_move(model: Model):

        max_score = -1
        final_choice = None

        for move, f in enumerate(options):
            copy = model.copy()
            score = get_move1_score(copy, f, DEPTH)
            if score > max_score:
                max_score = score
                final_choice = move

        return final_choice


def get_board_score(model, l):
    if l == 0:
        if not model.can_shift():
            return 0
        count = 1
        for i in range(4):
            for j in range(4):
                count += 1 if model.get_tile(i, j) == 0 else 0
        return count

    max_score = -1

    for option in options:
        copy = model.copy()
        max_score = max(get_move2_score(copy, option, l), max_score)

    return max_score



def get_move1_score(model, f, l):
    coordinates = f(model)

    if not coordinates:
        return -1
    
    score = 0

    for i, j, in coordinates:
        for next_tile in model.next_tile:
            copy = model.copy()
            copy.add_tile(next_tile, i, j)
            score += get_board_score(copy, l-1)
        
    score = score / (len(coordinates) * len(model.next_tile))

    return score


def get_move2_score(model: Model, f, l):
    coordinates = f(model)

    if not coordinates:
        return 0
    
    score = 0

    for i, j, in coordinates:
        for next_tile in [1, 2, 3]:
            copy = model.copy()
            copy.board.add_tile(next_tile, i, j)
            score += get_board_score(copy, l-1)
        
    score = score / (len(coordinates) * 3)

    return score



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