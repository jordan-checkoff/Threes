from game.Threes import Moves


class UserAgent:

    def choose_move(self, board, next_card):
        print(next_card)
        print("")
        print(board)

        while True:
            dir = input()
            if dir == "w":
                return Moves.UP
            elif dir == "a":
                return Moves.LEFT
            elif dir == "s":
                return Moves.DOWN
            elif dir == "d":
                return Moves.RIGHT
            else:
                print("input must be WASD")