
class Card:

    def __init__(self, val):
        self.value = val

    def can_combine(self, card):
        if self.value == 1:
            return True if card.value == 2 else False
        elif self.value == 2:
            return True if card.value == 1 else False
        else:
            return True if card.value == self.value else False
        
    def combine(self, card):
        if card:
            self.value += card.value

    def __str__(self):
        return str(self.value)