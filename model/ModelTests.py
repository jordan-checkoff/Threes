import unittest
from Model import Model


class ModelTests(unittest.TestCase):

    def test_init(self):
        board = [[1, 2, 3, 0],
                 [3, 0, 1, 2],
                 [1, 3, 0, 2],
                 [1, 2, 3, 0]]
        
        game = Model(board, 2)

        self.assertListEqual(game.board.board, board)
        self.assertEqual(game.next_card, 2)
        self.assertListEqual(game.deck.counts, [4, 3, 4])

    
    def test_update(self):
        board = [[1, 2, 3, 0],
                 [3, 0, 1, 2],
                 [1, 3, 0, 2],
                 [1, 2, 3, 0]]
        
        game = Model(board, 2)


        new_board = [[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]]

        game.update(new_board, 3)

        self.assertListEqual(game.board.board, new_board)
        self.assertEqual(game.next_card, 3)
        self.assertListEqual(game.deck.counts, [4, 3, 3])




if __name__ == '__main__':
    unittest.main()