from BoardFactory import BoardFactory
from CardFactory import CardFactory
import random

class Game:

    def __init__(self):
        self.card_factory = CardFactory()
        self.board_factory = BoardFactory()
    
    def play(self):
        board = self.board_factory.create_test_board()

        turn = 0

        while not board.is_full():
            next_card = self.card_factory.create_random_card(turn)

            print("\n")
            print(next_card)
            print("")
            print(board)

            dir = input()

            if dir == "w":
                options = board.shift_up()
                if options:
                    spot = self.pick_spot(options)
                    board.set_card(3, spot, next_card)
                    turn += 1

            if dir == "s":
                options = board.shift_down()
                if options:
                    spot = self.pick_spot(options)
                    board.set_card(0, spot, next_card)
                    turn += 1

            if dir == "a":
                options = board.shift_left()
                if options:
                    spot = self.pick_spot(options)
                    board.set_card(spot, 3, next_card)
                    turn += 1

            if dir == "d":
                options = board.shift_right()
                if options:
                    spot = self.pick_spot(options)
                    board.set_card(spot, 0, next_card)
                    turn += 1

        print("GAME OVER")


    def pick_spot(self, options):
        return random.choice(options)