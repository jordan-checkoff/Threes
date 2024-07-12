
class Board:

    def __init__(self, grid):
        self.grid = grid
 
    def shift_left(self):
        for i in range(4):
            for j in range(3):
                if not self.grid[i][j]:
                    self.shift_row_left(i, j)
                    break
                elif self.grid[i][j+1] and self.grid[i][j].can_combine(self.grid[i][j+1]):
                    self.grid[i][j].combine(self.grid[i][j+1])
                    self.shift_row_left(i, j+1)
                    break

    def shift_right(self):
        for i in range(4):
            for j in range(3, 0, -1):
                if not self.grid[i][j]:
                    self.shift_row_right(i, j)
                    break
                elif self.grid[i][j-1] and self.grid[i][j].can_combine(self.grid[i][j-1]):
                    self.grid[i][j].combine(self.grid[i][j-1])
                    self.shift_row_right(i, j-1)
                    break

    def shift_up(self):
        for j in range(4):
            for i in range(3):
                if not self.grid[i][j]:
                    self.shift_col_up(i, j)
                    break
                elif self.grid[i+1][j] and self.grid[i][j].can_combine(self.grid[i+1][j]):
                    self.grid[i][j].combine(self.grid[i+1][j])
                    self.shift_col_up(i+1, j)
                    break

    def shift_down(self):
        for j in range(4):
            for i in range(3, 0, -1):
                if not self.grid[i][j]:
                    self.shift_col_down(i, j)
                    break
                elif self.grid[i-1][j] and self.grid[i][j].can_combine(self.grid[i-1][j]):
                    self.grid[i][j].combine(self.grid[i-1][j])
                    self.shift_col_down(i-1, j)
                    break


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


    def get_value(self, i, j):
        return self.grid[i][j].value
    
    def set_card(self, i, j, card):
        self.grid[i][j] = card


    def __str__(self):
        output = ""

        for i in range(4):
            for j in range(4):
                if self.grid[i][j]:
                    val = self.get_value(i, j)
                    output += str(val) + " "
                else:
                    output += "  "
            output += "\n"

        return output