from model.Board import Board
import random
from controller.UserInterface import UserInterface
import agent.Expectimax as Expectimax

  
def play():

    ui = UserInterface()
    board, next = ui.get_state()

    model = Board(board, next)

    while True:
        dir = Expectimax.choose_move(model)
        ui.change_state(dir)

        board, next = ui.get_state()
        model.update(board, next)
        


if __name__ == "__main__":
    # play()
    print('a')