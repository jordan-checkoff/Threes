from game.Threes import Moves
import random


class OneStepAgent:

    def choose_move(self, board, next_card):
        options = {
            Moves.LEFT: lambda x: x.shift_left(),
            Moves.RIGHT: lambda x: x.shift_right(),
            Moves.UP: lambda x: x.shift_up(),
            Moves.DOWN: lambda x: x.shift_down(),
        }

        max_score = -1
        final_choice = None

        for move, f in options.items():
            score = self.get_score(board.copy(), next_card, f)
            if score > max_score:
                max_score = score
                final_choice = move

        return final_choice


    def get_score(self, board, next_card,  f):
        coordinates = f(board)

        if not coordinates:
            return -1
        
        total = 0

        for i, j, in coordinates:
            test = board.copy()
            test.add_tile(next_card, i, j)
            if test.can_shift():
                total += 1 / len(coordinates)

        return total