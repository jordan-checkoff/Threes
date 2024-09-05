from model.Model import Model
import random
from controller.UserInterface import UserInterface
import agent.agent as agent

  
def play():

    ui = UserInterface()
    board, next = ui.get_state()

    model = Model(board, next)

    for i in range(20):
        dir = agent.choose_move(model)
        ui.change_state(dir)

        board, next = ui.get_state()
        model.update(board, next)
        


if __name__ == "__main__":
    play()