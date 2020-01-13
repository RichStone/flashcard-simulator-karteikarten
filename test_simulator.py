import unittest
from simulator import Simulator, Card


class TestSimulator(unittest.TestCase):
    def test_card_tracks_(self):
        card = Card()
        Simulator.learned(card)
        Simulator.learned(card)
        self.assertEqual(card.learn_progress, 2)


if __name__ == '__main__':
    unittest.main()
