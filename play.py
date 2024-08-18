from Game import Game, Moves
from BoardFactory import BoardFactory


def start_game():
    factory = BoardFactory()
    board = factory.create_test_board()
    game = Game(board)
    game.play(decider, True)


def decider(board, next_card):
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


if __name__ == "__main__":
    start_game()



# Get rid of cards
# Update options set formation in Board on shift to include ordered pair (tuple) of where they can go
# Update Game to reflect that
# Write tests
# Write new AI to see if there is only one option where the thing can go and if so, add it there and see if that ends the game