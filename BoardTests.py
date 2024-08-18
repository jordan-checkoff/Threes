import unittest
from Board import Board


class BoardTests(unittest.TestCase):

    def test_shift_left(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 1, 0],
                       [3, 3, 0, 2]])
        
        coordinates = board.shift_left()

        expected = [[3, 2, 1, 0],
                    [3, 0, 1, 0],
                    [3, 3, 0, 0],
                    [6, 0, 2, 0]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, {(3, 0), (3, 1), (3, 2), (3, 3)})


    def test_shift_down(self):
        board = Board([[0, 3, 2, 1],
                       [0, 1, 0, 1],
                       [2, 2, 1, 3],
                       [3, 1, 0, 2]])
        
        coordinates = board.shift_down()

        expected = [[0, 0, 0, 1],
                    [0, 3, 2, 1],
                    [2, 1, 0, 3],
                    [3, 3, 1, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, {(1, 0), (2, 0)})


    def test_shift_right(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 6, 3],
                       [0, 1, 0, 2]])
        
        coordinates = board.shift_right()

        expected = [[0, 0, 3, 3],
                    [0, 2, 1, 1],
                    [3, 2, 6, 3],
                    [0, 0, 1, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, {(0, 0), (0, 1), (0, 3)})


    def test_shift_up(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 1, 3],
                       [0, 1, 0, 2]])
        
        coordinates = board.shift_up()

        expected = [[2, 3, 2, 1],
                    [3, 3, 1, 1],
                    [0, 1, 0, 3],
                    [0, 0, 0, 2]]

        self.assertEqual(board.board, expected)

        self.assertEqual(coordinates, {(0, 3), (1, 3), (2, 3)})


    def test_can_shift(self):
        board1 = Board([[0, 3, 2, 1],
                        [2, 1, 0, 1],
                        [3, 2, 1, 0],
                        [0, 1, 0, 2]])
        
        self.assertTrue(board1.can_shift())


        board2 = Board([[1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]])
        
        self.assertFalse(board2.can_shift())


        board3 = Board([[1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 0, 1],
                        [1, 1, 1, 1]])
        
        self.assertTrue(board3.can_shift())


        board4 = Board([[0, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]])
        
        self.assertTrue(board4.can_shift())     


    def test_str(self):
        board = Board([[0, 3, 2, 1],
                       [2, 1, 0, 1],
                       [3, 2, 1, 0],
                       [0, 1, 0, 2]])
                
        self.assertEqual(str(board), "0\t3\t2\t1\n2\t1\t0\t1\n3\t2\t1\t0\n0\t1\t0\t2")


if __name__ == '__main__':
    unittest.main()