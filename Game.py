from BoardFactory import BoardFactory
from CardFactory import CardFactory
import random

class Game:

    def __init__(self):
        self.card_factory = CardFactory()
        self.board_factory = BoardFactory()
        self.board = self.board_factory.create_test_board()
    
    def play(self):

        turn = 0

        while not self.is_game_over():
            next_card = self.card_factory.create_random_card(turn)

            print("\n")
            print(next_card)
            print("")
            print(self.board)

            dir = input()

            if dir == "w":
                options = self.board.shift_up()
                if options:
                    spot = self.pick_spot(options)
                    self.board.set_card(3, spot, next_card)
                    turn += 1

            if dir == "s":
                options = self.board.shift_down()
                if options:
                    spot = self.pick_spot(options)
                    self.board.set_card(0, spot, next_card)
                    turn += 1

            if dir == "a":
                options = self.board.shift_left()
                if options:
                    spot = self.pick_spot(options)
                    self.board.set_card(spot, 3, next_card)
                    turn += 1

            if dir == "d":
                options = self.board.shift_right()
                if options:
                    spot = self.pick_spot(options)
                    self.board.set_card(spot, 0, next_card)
                    turn += 1

        print("GAME OVER")


    def is_game_over(self):
        if not (self.board.can_shift_down() or
                self.board.can_shift_up() or
                self.board.can_shift_left() or
                self.board.can_shift_right()):
            return True
        else:
            return False


    def pick_spot(self, options):
        return random.choice(options)