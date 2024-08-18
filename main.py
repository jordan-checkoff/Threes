from game.Threes import Threes
from game.BoardFactory import BoardFactory
from agents.UserAgent import UserAgent
from agents.RandomAgent import RandomAgent


def start_game():
    factory = BoardFactory()
    board = factory.create_test_board()

    game = Threes(board)
    agent = UserAgent()
    game.play(agent)



if __name__ == "__main__":
    start_game()