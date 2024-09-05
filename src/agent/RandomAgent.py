import random


class RandomAgent:

    def choose_move(self, board, next_card):
        i = random.randint(0, 3)
        return i