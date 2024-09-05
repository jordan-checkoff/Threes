from model.Board import Board
from model.Deck import Deck
from enum import Enum


class Model:

    def __init__(self, board, next_tile):
        self.board = Board(board)
        self.next_tile = next_tile
        self.deck = Deck(next_tile)

    def update(self, board, next_tile):
        self.board = Board(board)
        self.next_tile = next_tile
        self.deck.remove_card(next_tile)

class Moves(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4