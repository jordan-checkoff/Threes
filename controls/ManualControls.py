
class ManualControls:

    def get_board(self):
        board = []
        for i in range(4):
            s = input(f"Enter row {i+1}: ")
            row = [int(x) for x in s.split()]
            board.append(row)

        return board
    
    def get_position(self):
        i = input("Enter row number: ")
        j = input("Enter column number: ")

        return (int(i), int(j))
    
    def get_next_tile(self):
        tile = input("Enter next tile: ")
        return int(tile)
    
    def make_move(self, move):
        print(move.name)