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



    def can_shift(self, i, j, x, y):
        curr = self.get_card(i, j)
        neighbor = self.get_card(x, y)

        if not curr and neighbor:
            return True
        if curr and curr.can_combine(neighbor):
            return True
        return False

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
        options = []
        for i in range(4):
            for j in range(3):
                if not self.grid[i][j] and self.grid[i][j+1]:
                    self.shift_row_left(i, j)
                    options.append(i)
                    break
                elif self.grid[i][j+1] and self.grid[i][j].can_combine(self.grid[i][j+1]):
                    self.grid[i][j].combine(self.grid[i][j+1])
                    self.shift_row_left(i, j+1)
                    options.append(i)
                    break
        return options

    def shift_right(self):
        options = []
        for i in range(4):
            for j in range(3, 0, -1):
                if not self.grid[i][j] and self.grid[i][j-1]:
                    self.shift_row_right(i, j)
                    options.append(i)
                    break
                elif self.grid[i][j-1] and self.grid[i][j].can_combine(self.grid[i][j-1]):
                    self.grid[i][j].combine(self.grid[i][j-1])
                    self.shift_row_right(i, j-1)
                    options.append(i)
                    break
        return options

    def shift_up(self):
        options = []
        for j in range(4):
            for i in range(3):
                if not self.grid[i][j] and self.grid[i+1][j]:
                    self.shift_col_up(i, j)
                    options.append(j)
                    break
                elif self.grid[i+1][j] and self.grid[i][j].can_combine(self.grid[i+1][j]):
                    self.grid[i][j].combine(self.grid[i+1][j])
                    self.shift_col_up(i+1, j)
                    options.append(j)
                    break
        return options

    def shift_down(self):
        options = []
        for j in range(4):
            for i in range(3, 0, -1):
                if not self.grid[i][j] and self.grid[i-1][j]:
                    self.shift_col_down(i, j)
                    options.append(j)
                    break
                elif self.grid[i-1][j] and self.grid[i][j].can_combine(self.grid[i-1][j]):
                    self.grid[i][j].combine(self.grid[i-1][j])
                    self.shift_col_down(i-1, j)
                    options.append(j)
                    break
        return options


    def shift_row_left(self, i, j):
        for col in range(j, 3):
            self.grid[i][col] = self.grid[i][col+1]
        self.grid[i][3] = None

    def shift_row_right(self, i, j):
        for col in range(j, 0, -1):
            self.grid[i][col] = self.grid[i][col-1]
        self.grid[i][0] = None

    def shift_col_up(self, i, j):
        for row in range(i, 3):
            self.grid[row][j] = self.grid[row+1][j]
        self.grid[3][j] = None

    def shift_col_down(self, i, j):
        for row in range(i, 0, -1):
            self.grid[row][j] = self.grid[row-1][j]
        self.grid[0][j] = None


    def __str__(self):
        horizontal = "-" * (CARD_WIDTH*3 + 4) + "\n"
        vertical = ("|" + (" " * CARD_WIDTH)) * 3 + "|\n"

        output = horizontal + vertical
        output += f"|{self.get_padded(0, 0)}|{self.get_padded(0, 1)}|{self.get_padded(0, 2)}|\n"
        output += vertical + horizontal + vertical
        output += f"|{self.get_padded(1, 0)}|{self.get_padded(1, 1)}|{self.get_padded(1, 2)}|\n"
        output += vertical + horizontal + vertical
        output += f"|{self.get_padded(2, 0)}|{self.get_padded(2, 1)}|{self.get_padded(2, 2)}|\n"
        output += vertical + horizontal

        return output
    

    def get_padded(self, i, j):
        if self.grid[i][j]:
            return self.grid[i][j].pad_value()
        else:
            return " " * CARD_WIDTH