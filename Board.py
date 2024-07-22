from Card import CARD_WIDTH

class Board:

    def __init__(self, grid):
        self.grid = grid

    def has_card(self, i, j):
        return True if self.grid[i][j] else False

    def get_card(self, i, j):
        return self.grid[i][j]
    
    def get_value(self, i, j):
        return self.get_card(i, j).value if self.has_card(i, j) else None
    
    def set_card(self, i, j, card):
        self.grid[i][j] = card

    def remove_card(self, i, j):
        self.grid[i][j] = None

    def move_card(self, i, j, x, y):
        card = self.get_card(x, y)
        self.set_card(i, j, card)
        self.remove_card(x, y)

    def combine_cards(self, i, j, x, y):
        curr = self.get_card(i, j)
        neighbor = self.get_card(x, y)
        curr.combine(neighbor)
        self.remove_card(x, y)



    def can_shift(self, i, j, x, y):
        curr = self.get_card(i, j)
        neighbor = self.get_card(x, y)

        if not curr and neighbor:
            return True
        if curr and curr.can_combine(neighbor):
            return True
        return False
    
    def shift(self, i, j, x, y):
        curr = self.get_card(i, j)
        neighbor = self.get_card(x, y)

        if not curr and neighbor:
            self.move_card(i, j, x, y)
            return True
        if curr and curr.can_combine(neighbor):
            self.combine_cards(i, j, x, y)
            return True



    def can_shift_left(self):
        for i in range(4):
            for j in range(3):
                if self.can_shift(i, j, i, j+1):
                    return True
        return False
    
    def can_shift_right(self):
        for i in range(4):
            for j in range(3, 0, -1):
                if self.can_shift(i, j, i, j-1):
                    return True
        return False
    
    def can_shift_up(self):
        for j in range(4):
            for i in range(3):
                if self.can_shift(i, j, i+1, j):
                    return True
        return False
    
    def can_shift_down(self):
        for j in range(4):
            for i in range(3, 0, -1):
                if self.can_shift(i, j, i-1, j):
                    return True
        return False
       

 
    def shift_left(self):
        options = set()
        for i in range(4):
            for j in range(3):
                if self.shift(i, j, i, j+1):
                    options.add(i)
        return options

    def shift_right(self):
        options = set()
        for i in range(4):
            for j in range(3, 0, -1):
                if self.shift(i, j, i, j-1):
                    options.add(i)
        return options
    
    def shift_up(self):
        options = set()
        for j in range(4):
            for i in range(3):
                if self.shift(i, j, i+1, j):
                    options.add(j)
        return options
    
    def shift_down(self):
        options = set()
        for j in range(4):
            for i in range(3, 0, -1):
                if self.shift(i, j, i-1, j):
                    options.add(j)
        return options


    def __str__(self):
        horizontal = "-" * (CARD_WIDTH*4 + 5) + "\n"
        vertical = ("|" + (" " * CARD_WIDTH)) * 4 + "|\n"

        output = horizontal + vertical
        output += f"|{self.get_padded(0, 0)}|{self.get_padded(0, 1)}|{self.get_padded(0, 2)}|{self.get_padded(0, 3)}|\n"
        output += vertical + horizontal + vertical
        output += f"|{self.get_padded(1, 0)}|{self.get_padded(1, 1)}|{self.get_padded(1, 2)}|{self.get_padded(1, 3)}|\n"
        output += vertical + horizontal + vertical
        output += f"|{self.get_padded(2, 0)}|{self.get_padded(2, 1)}|{self.get_padded(2, 2)}|{self.get_padded(2, 3)}|\n"
        output += vertical + horizontal + vertical
        output += f"|{self.get_padded(3, 0)}|{self.get_padded(3, 1)}|{self.get_padded(3, 2)}|{self.get_padded(3, 3)}|\n"
        output += vertical + horizontal

        return output
    

    def get_padded(self, i, j):
        if self.grid[i][j]:
            return self.grid[i][j].pad_value()
        else:
            return " " * CARD_WIDTH