import unittest
from model.Board import Board
from model.Directions import Directions


class BoardTests(unittest.TestCase):

    def test_shift_left(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 1, 0],
                       [3, 3, 0, 2]])
        
        coordinates = board.shift(Directions.LEFT)

        expected = [[3, 2, 1, 0],
                    [3, 0, 1, 0],
                    [3, 3, 0, 0],
                    [6, 0, 2, 0]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, [(0, 3), (1, 3), (2, 3), (3, 3)])


    def test_shift_down(self):
        board = Board([[0, 3, 2, 1],
                       [0, 1, 0, 1],
                       [2, 2, 1, 3],
                       [3, 1, 0, 2]])
        
        coordinates = board.shift(Directions.DOWN)

        expected = [[0, 0, 0, 1],
                    [0, 3, 2, 1],
                    [2, 1, 0, 3],
                    [3, 3, 1, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, [(0, 1), (0, 2)])


    def test_shift_right(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 6, 3],
                       [0, 1, 0, 2]])
        
        coordinates = board.shift(Directions.RIGHT)

        expected = [[0, 0, 3, 3],
                    [0, 2, 1, 1],
                    [3, 2, 6, 3],
                    [0, 0, 1, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, [(0, 0), (1, 0), (3, 0)])


    def test_shift_up(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 1, 3],
                       [0, 1, 0, 2]])
        
        coordinates = board.shift(Directions.UP)

        expected = [[2, 3, 2, 1],
                    [3, 3, 1, 1],
                    [0, 1, 0, 3],
                    [0, 0, 0, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, [(3, 0), (3, 1), (3, 2)])

if __name__ == '__main__':
    unittest.main()