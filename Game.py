import random
from enum import Enum

class Game:

    def __init__(self, board):

        self.turn = 0
        self.board = board
        self.get_next_card()
    
    def play(self, decider, p=False):

        while self.board.can_shift():

            if p:
                print("\n")
                print(self.next_card)
                print("")
                print(self.board)

            dir = decider(self.board, self.next_card)

            coordinates = None

            if dir == Moves.UP:
                coordinates = self.board.shift_up()
            elif dir == Moves.DOWN:
                coordinates = self.board.shift_down()
            elif dir == Moves.LEFT:
                coordinates = self.board.shift_left()
            elif dir == Moves.RIGHT:
                coordinates = self.board.shift_right()
            else:
                print("Move must be WASD")

            if coordinates:
                choice = random.choice(list(coordinates))
                self.board.add_tile(self.next_card, choice[0], choice[1])
                self.turn += 1
                self.get_next_card()
            elif p:
                print("Invalid move")

        print("GAME OVER")
        print(f"Turns: {self.turn}")
        print(self.board)



    def get_next_card(self):
        self.next_card = random.choice([1, 2, 3])

    def pick_spot(self, options):
        return random.choice(list(options))
    



class Moves(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4