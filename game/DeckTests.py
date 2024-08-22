import unittest
from Deck import Deck


class BoardTests(unittest.TestCase):

    def test_init(self):
        deck = Deck()
        self.assertListEqual(deck.counts, [4, 4, 4])


    def test_draw(self):
        deck = Deck()
        deck.draw_card()
        deck.draw_card()
        self.assertEqual(sum(deck.counts), 10)

    def test_complete_draw(self):
        deck = Deck()
        cards = [0, 0, 0]
        for _ in range(12):
            card = deck.draw_card()
            cards[card-1] += 1

        self.assertListEqual(cards, [4, 4, 4])
        self.assertListEqual(deck.counts, [4, 4, 4])




if __name__ == '__main__':
    unittest.main()