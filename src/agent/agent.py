

DEPTH = 4


options = [
    lambda x: x.shift_up(),
    lambda x: x.shift_right(),
    lambda x: x.shift_down(),
    lambda x: x.shift_left(),
]

def choose_move(model):

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
        if not model.board.can_shift():
            return 0
        count = 1
        for i in range(4):
            for j in range(4):
                count += 1 if model.board.get_tile(i, j) == 0 else 0
        return count

    max_score = -1

    for option in options:
        copy = model.copy()
        max_score = max(get_move2_score(copy, option, l), max_score)

    return max_score



def get_move1_score(model, f, l):
    coordinates = f(model.board)

    if not coordinates:
        return -1
    
    score = 0

    for i, j, in coordinates:
        for next_tile in model.next_tile:
            copy = model.copy()
            copy.board.add_tile(next_tile, i, j)
            score += get_board_score(copy, l-1)
        
    score = score / (len(coordinates) * len(model.next_tile))

    return score


def get_move2_score(model, f, l):
    coordinates = f(model.board)

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