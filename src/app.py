from model.Board import Board
import random
from controller.UserInterface import UserInterface
from agent.Agent import expectimax

  
def play():

    ui = UserInterface()

    while True:
        board, next = ui.get_state()
        model = Board(board)
        dir = expectimax(model, next)
        ui.change_state(dir)
        


if __name__ == "__main__":
    play()