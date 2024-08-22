import random

class Deck():
    
    def __init__(self, next_card):
        self.reset()
        self.remove_card(next_card)

    def reset(self):
        self.counts = [4, 4, 4]

    def remove_card(self, next_card):
        self.counts[next_card - 1] -= 1
        if sum(self.counts) == 0:
            self.reset()