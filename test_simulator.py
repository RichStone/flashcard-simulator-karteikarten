import unittest
from simulator import Simulator, Card


class TestSimulator(unittest.TestCase):
    def test_card_tracks_progress_after_2_learned_successes(self):
        card = Card()
        Simulator.learned(card)
        Simulator.learned(card)
        self.assertEqual(card.learn_progress, 2)

    def test_card_resets_progress_after_a_fail(self):
        card = Card()
        Simulator.learned(card)
        Simulator.learned(card)
        Simulator.forgot(card)
        self.assertEqual(card.learn_progress, 0)


if __name__ == '__main__':
    unittest.main()
