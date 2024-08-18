from game.Threes import Moves
import random


class RandomAgent:

    def choose_move(self, board, next_card):
        options = list(Moves)
        i = random.randint(0, 3)
        choice = options[i]
        return choice