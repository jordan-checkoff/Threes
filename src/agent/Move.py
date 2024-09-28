from model.Directions import Directions

class Move:

    def __init__(self, dir: Directions, score: float):
        self.dir = dir
        self.score = score
