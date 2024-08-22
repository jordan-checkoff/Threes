import unittest
from unittest import mock
from ManualControls import ManualControls


class ManualControlsasTests(unittest.TestCase):
    @mock.patch('ManualControls.input', create=True)
    def test_get_board(self, mocked_input):
        mocked_input.side_effect = ["0 3 2 3", "1 2 3 0", "3 2 1 0", "1 3 2 1"]
        controls = ManualControls()
        board = controls.get_board()

        self.assertListEqual(board, [[0, 3, 2, 3], [1, 2, 3, 0], [3, 2, 1, 0], [1, 3, 2, 1]])

    @mock.patch('ManualControls.input', create=True)
    def test_get_position(self, mocked_input):
        mocked_input.side_effect = ["1", "2"]
        controls = ManualControls()
        pos = controls.get_position()

        self.assertTupleEqual(pos, (1, 2))

    @mock.patch('ManualControls.input', create=True)
    def test_get_next_tile(self, mocked_input):
        mocked_input.side_effect = "6"
        controls = ManualControls()
        tile = controls.get_next_tile()

        self.assertEqual(tile, 6)




if __name__ == '__main__':
    unittest.main()