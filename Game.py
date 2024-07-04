from Board import Board
from Card import Card

class Game:

    def __init__(self):
        self.board = Board([[Card(2), Card(3), None, None],
                    [None, None, Card(1), Card(1)],
                    [Card(1), None, Card(3), None],
                    [Card(2), Card(1), None, Card(2)]])
        
    
    def play(self):
        while True:
            print(self.board)

            dir = input()

            if dir == "w":
                self.board.shift_up()

            if dir == "s":
                self.board.shift_down()

            if dir == "a":
                self.board.shift_left()

            if dir == "d":
                self.board.shift_right()
