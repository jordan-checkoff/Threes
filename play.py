from Game import Game


def start_game():
    game = Game()
    game.play(decider)


def decider(board, next_card):
    dir = input()
    return dir


if __name__ == "__main__":
    start_game()