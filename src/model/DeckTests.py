import unittest
from Deck import Deck


class DeckTests(unittest.TestCase):

    def test_init(self):
        deck = Deck(3)
        self.assertListEqual(deck.counts, [4, 4, 3])

    def test_reset(self):
        deck = Deck(2)
        deck.remove_card(1)
        deck.reset()
        self.assertListEqual(deck.counts, [4, 4, 4])

    def test_remove_card(self):
        deck = Deck(2)
        deck.remove_card(1)
        self.assertEqual(deck.counts, [3, 3, 4])

        for _ in range(3):
            deck.remove_card(1)
        for _ in range(3):
            deck.remove_card(2)
        for _ in range(4):
            deck.remove_card(3)

        self.assertListEqual(deck.counts, [4, 4, 4])




if __name__ == '__main__':
    unittest.main()