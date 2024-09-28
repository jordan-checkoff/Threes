
class Board:

    def __init__(self, board):
        self.board = [row[:] for row in board]


    def add_tile(self, tile, x, y):
        self.board[y][x] = tile

    def get_tile(self, i, j):
        return self.board[i][j]
    

    def num_cards(self):
        count = 0
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0:
                    count += 1

        return count


    def can_combine(self, val1, val2):
        if val1 == 0:
            return True if val2 != 0 else False
        elif val1 == 1:
            return True if val2 == 2 else False
        elif val1 == 2:
            return True if val2 == 1 else False
        else:
            return True if val1 == val2 else False
        


    def can_shift(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return True
                if i < 3 and self.can_combine(self.board[i][j], self.board[i+1][j]):
                    return True
                if j < 3 and self.can_combine(self.board[i][j], self.board[i][j+1]):
                    return True


    def shift(self, x1, x2, x_dir, y1, y2, y_dir, dx, dy):
        coordinates = set()

        for i in range(y1, y2, y_dir):
            for j in range(x1, x2, x_dir):
                if self.can_combine(self.board[i+dy][j+dx], self.board[i][j]):
                    self.board[i+dy][j+dx] += self.board[i][j]
                    self.board[i][j] = 0
                    if dx:
                        coordinates.add((x2 + dx, i))
                    else:
                        coordinates.add((j, y2 + dy))

        return coordinates

    
    def shift_left(self):
        return self.shift(1, 4, 1, 0, 4, 1, -1, 0)

    def shift_right(self):
        return self.shift(2, -1, -1, 0, 4, 1, 1, 0)

    def shift_up(self):
        return self.shift(0, 4, 1, 1, 4, 1, 0, -1)

    def shift_down(self):
        return self.shift(0, 4, 1, 2, -1, -1, 0, 1)
    

    def copy(self):
        return self.board


    def __str__(self):
        stringified = [[str(tile) for tile in row] for row in self.board]
        return "\n".join(["\t".join(row) for row in stringified])