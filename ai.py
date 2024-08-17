from Game import Game
import random


def run_ai():
    game = Game()
    game.play(decider)


def decider(board, next_card):
    options = ["w", "a", "s", "d"]
    i = random.randint(0, 3)
    choice = options[i]
    return choice


if __name__ == "__main__":
    run_ai()