

class Deck():
    
    def __init__(self, next_card):
        self.reset()
        self.remove_card(next_card)

    def reset(self):
        self.counts = [4, 4, 4]

    def remove_card(self, next_card):
        if next_card[0] <= 3:
            self.counts[next_card[0] - 1] -= 1
            if sum(self.counts) == 0:
                self.reset()

    def copy(self):
        copy = Deck([1])
        copy.counts = [x for x in self.counts]
        return copy