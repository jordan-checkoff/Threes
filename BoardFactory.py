from Board import Board

class BoardFactory:

    def create_board(self, board):
        return Board(board)
    

    def create_test_board(self):
        grid = [[2, 3, 0, 0],
                [0, 0, 1, 1],
                [1, 0, 3, 0],
                [2, 1, 0, 2]]
        
        return self.create_board(grid)
    
    def copy_board(self, board):
        grid = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(board.get_tile(i, j))
            grid.append(row)

        return self.create_board(grid)