import random;
from CardFactory import CardFactory;

class Board:

    def __init__(self):
        self.generator = CardFactory()
        self.initialize_grid()


    def initialize_grid(self):
        self.grid = [[None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None],
                     [None, None, None, None]]
        
        for i in range(4):
            for j in range(4):
                val = random.randint(0,1)
                self.grid[i][j] = self.generator.create_random_card() if val == 1 else self.generator.create_null_card()



    def get_value(self, i, j):
        return self.grid[i][j].value


    def __str__(self):
        output = ""
        for i in range(4):
            for j in range(4):
                val = self.get_value(i, j)
                if val > 0:
                    output += str(val) + " "
                else:
                    output += "  "
            output += "\n"

        return output