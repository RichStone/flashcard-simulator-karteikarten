import unittest
from simulator import Simulator, Card


class TestSimulator(unittest.TestCase):
    def test_card_tracks_correct_count(self):
        card = Card()
        Simulator.learn(card)
        Simulator.learn(card)
        self.assertEqual(card.learn_success, 2)


if __name__ == '__main__':
    unittest.main()
