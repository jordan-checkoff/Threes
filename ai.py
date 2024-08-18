from Game import Game, Moves
from BoardFactory import BoardFactory
import random


def run_ai():
    factory = BoardFactory()
    board = factory.create_test_board()
    game = Game(board)
    game.play(decider)


def decider(board, next_card):
    options = list(Moves)
    i = random.randint(0, 3)
    choice = options[i]
    return choice


if __name__ == "__main__":
    run_ai()