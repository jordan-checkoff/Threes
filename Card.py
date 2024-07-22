
CARD_WIDTH = 6

class Card:

    def __init__(self, val):
        self.value = val

    def can_combine(self, card):
        if not card:
            return False
        
        if self.value == 1:
            return True if card.value == 2 else False
        elif self.value == 2:
            return True if card.value == 1 else False
        else:
            return True if card.value == self.value else False
        
    def combine(self, card):
        if card:
            self.value += card.value

    def pad_value(self):
        str_val = str(self.value)
        diff = CARD_WIDTH - len(str_val)
        
        right_pad = diff // 2
        left_pad = diff - right_pad

        return " " * left_pad + str_val + " " * right_pad

    def __str__(self):
        horizontal = "-" * (CARD_WIDTH + 2) + "\n"
        vertical = "|" + " " * CARD_WIDTH + "|\n"

        output = horizontal + vertical
        output += "|" + self.pad_value() + "|\n"
        output += vertical + horizontal

        return output