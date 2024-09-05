from src.Game import Game
from src.controller.Controls import Controls;
from agents.RandomAgent import RandomAgent


def start_game():
    controls = Controls()
    agent = RandomAgent()

    game = Game(controls, agent)

    game.play()




if __name__ == "__main__":
    start_game()