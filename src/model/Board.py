from model.Directions import Directions

class Board:

    def __init__(self, board):
        self.board = [row[:] for row in board]

    def add_tile(self, tile, i, j):
        self.board[i][j] = tile

    def get_tile(self, i, j):
        return self.board[i][j]

    def can_combine(self, val1, val2):
        if val1 == 0:
            return True if val2 != 0 else False
        elif val1 == 1:
            return True if val2 == 2 else False
        elif val1 == 2:
            return True if val2 == 1 else False
        else:
            return True if val1 == val2 else False

    def shift(self, dir: Directions):
        coordinates = []

        match dir:
            case Directions.UP:
                self.shift_up(coordinates)
            case Directions.DOWN:
                self.shift_down(coordinates)
            case Directions.LEFT:
                self.shift_left(coordinates)
            case Directions.RIGHT:
                self.shift_right(coordinates)

        return coordinates

    
    def shift_left(self, coordinates):
        for i in range(4):
            combined = False
            for j in range(3):
                if self.can_combine(self.board[i][j], self.board[i][j+1]):
                    combined = True
                    self.board[i][j] += self.board[i][j+1]
                    self.board[i][j+1] = 0
            if combined:
                coordinates.append((i, 3))

    def shift_right(self, coordinates):
        for i in range(4):
            combined = False
            for j in range(3, 0, -1):
                if self.can_combine(self.board[i][j], self.board[i][j-1]):
                    combined = True
                    self.board[i][j] += self.board[i][j-1]
                    self.board[i][j-1] = 0
            if combined:
                coordinates.append((i, 0))

    def shift_up(self, coordinates):
        for j in range(4):
            combined = False
            for i in range(3):
                if self.can_combine(self.board[i][j], self.board[i+1][j]):
                    combined = True
                    self.board[i][j] += self.board[i+1][j]
                    self.board[i+1][j] = 0
            if combined:
                coordinates.append((3, j))

    def shift_down(self, coordinates):
        for j in range(4):
            combined = False
            for i in range(3, 0, -1):
                if self.can_combine(self.board[i][j], self.board[i-1][j]):
                    combined = True
                    self.board[i][j] += self.board[i-1][j]
                    self.board[i-1][j] = 0
            if combined:
                coordinates.append((0, j))
    

    def copy(self):
        return Board(self.board)