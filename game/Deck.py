import random

class Deck():
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.counts = [4, 4, 4]

    def draw_card(self):
        card = random.choices([1, 2, 3], self.counts)[0]
        self.counts[card-1] -= 1

        if sum(self.counts) == 0:
            self.reset()

        return card
