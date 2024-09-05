from model.Model import Model

class Game():

    def __init__(self, controls, agent):
        self.controls = controls
        self.agent = agent

    
    def play(self):
        board = self.controls.get_board()
        next_tile = self.controls.get_next_tile()

        model = Model(board, next_tile)

        while True:
            decision = self.agent.choose_move(model)
            self.controls.make_move(decision)
            
            board = self.controls.get_board()
            next_tile = self.controls.get_next_tile()
            model.update(board, next_tile)