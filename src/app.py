from model.Board import Board
from controller.UserInterface import UserInterface
from agent.Agent import expectimax

  
def play():

    ui = UserInterface()

    while True:
        state = ui.get_state()
        dir = expectimax(Board(state["board"]), state["next_tile"])
        ui.change_state(dir)
        


if __name__ == "__main__":
    play()