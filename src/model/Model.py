from __future__ import annotations
from model.Board import Board
from model.Deck import Deck
from enum import Enum


class Model:

    def __init__(self, board: Board, next_tile: int):
        self.board = Board(board)
        self.next_tile = next_tile
        self.deck = Deck(next_tile)

    def update(self, board: Board, next_tile: int) -> None:
        self.board = Board(board)
        self.next_tile = next_tile
        self.deck.remove_card(next_tile)

    def copy(self) -> Model:
        copy = Model(self.board.copy(), self.next_tile)
        copy.deck = self.deck.copy()
        return copy
    
    def shift_left(self):
        return self.board.shift_left()

    def shift_down(self):
        return self.board.shift_down()

    def shift_up(self):
        return self.board.shift_up()

    def shift_right(self):
       return self.board.shift_right()

    def add_tile(self, tile: int, x: int, y: int) -> None:
        self.board.add_tile(tile, x, y)

    def can_shift(self):
        return self.board.can_shift()
    
    def get_tile(self, i: int, j: int):
        return self.board.get_tile(i, j)
    
    def get_counts(self):
        return self.deck.counts
    
    def remove_card(self, card: int):
        self.deck.remove_card(card)

    def num_cards(self):
        return self.board.num_cards()

class Moves(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4