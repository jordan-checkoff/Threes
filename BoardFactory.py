from Board import Board
from CardFactory import CardFactory


class BoardFactory:

    def __init__(self):
        self.card_factory = CardFactory()

    def create_board(self, board):
        grid = [[self.card_factory.create_card(val) for val in row] for row in board]

        return Board(grid)
    

    def create_test_board(self):
        grid = [[2, 3, None, None],
                [None, None, 1, 1],
                [1, None, 3, None],
                [2, 1, None, 2]]
        
        return self.create_board(grid)