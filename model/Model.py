from Board import Board
from Deck import Deck


class Model:

    def __init__(self, board, next_card):
        self.board = Board(board)
        self.next_card = next_card
        self.deck = Deck(next_card)

    def update(self, board, next_card):
        self.board = Board(board)
        self.next_card = next_card
        self.deck.remove_card(next_card)