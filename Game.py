from BoardFactory import BoardFactory

class Game:

    def __init__(self):
        self.board_factory = BoardFactory()
    
    def play(self):
        board = self.board_factory.create_test_board()

        while True:
            print(board)

            dir = input()

            if dir == "w":
                board.shift_up()

            if dir == "s":
                board.shift_down()

            if dir == "a":
                board.shift_left()

            if dir == "d":
                board.shift_right()
