from BoardFactory import BoardFactory
from CardFactory import CardFactory
import random

class Game:

    def __init__(self):
        self.card_factory = CardFactory()
        self.board_factory = BoardFactory()

        self.turn = 0

        self.board = self.board_factory.create_test_board()
        self.next_card = self.card_factory.create_random_card(self.turn)
    
    def play(self, decider, p=False):

        while not self.board.is_unshiftable():

            if p:
                print("\n")
                print(self.next_card)
                print("")
                print(self.board)

            dir = decider(self.board, self.next_card)

            if dir == "w":
                f = self.board.shift_up
                g = lambda x: self.board.set_card(3, x, self.next_card)
                if not self.attempt_move(f, g) and p:
                    print("Invalid move")

            elif dir == "s":
                f = self.board.shift_down
                g = lambda x: self.board.set_card(0, x, self.next_card)
                if not self.attempt_move(f, g) and p:
                    print("Invalid move")

            elif dir == "a":
                f = self.board.shift_left
                g = lambda x: self.board.set_card(x, 3, self.next_card)
                if not self.attempt_move(f, g) and p:
                    print("Invalid move")

            elif dir == "d":
                f = self.board.shift_right
                g = lambda x: self.board.set_card(x, 0, self.next_card)
                if not self.attempt_move(f, g) and p:
                    print("Invalid move")

            else:
                print("Move must be WASD")

        print("GAME OVER")
        print(f"Turns: {self.turn}")
        print(self.board)


    def attempt_move(self, f, g):
        options = f()
        if options:
            spot = self.pick_spot(options)
            g(spot)
            self.turn += 1
            self.next_card = self.card_factory.create_random_card(self.turn)
            return True
        else:
            return False


    def pick_spot(self, options):
        return random.choice(list(options))