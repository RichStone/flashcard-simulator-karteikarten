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

    def test_simulator_finds_1_card_on_day_1(self):
        simulator = Simulator(card_amount=1)
        cards = simulator.get_cards(day_idx=0)
        self.assertEqual(len(cards), 1)

    def test_simulator_has_365_cards_on_init(self):
        simulator = Simulator(card_amount=365)
        for cards in simulator.days:
            self.assertEqual(len(cards), 1)
        self.assertEqual(len(simulator.days), 365)

    def test_learned_first_day_card_appears_in_3_days(self):
        simulator = Simulator(card_amount=10)
        first_card = simulator.get_cards(day_idx=0)[0]
        simulator.learn(day=0)
        day_3_cards = simulator.get_cards(day_idx=3)
        first_card_found_in_day_3 = False
        for card in day_3_cards:
            if card.id == first_card.id:
                first_card_found_in_day_3 = True
        self.assertTrue(first_card_found_in_day_3)

    def test_learned_first_day_card_appears_on_day_10_after_2_learns(self):
        simulator = Simulator(card_amount=15)
        first_card = simulator.get_cards(day_idx=0)[0]
        simulator.learn(day=0)
        simulator.learn(day=3)
        day_10_cards = simulator.get_cards(day_idx=10)
        first_card_found_in_day_10 = False
        for card in day_10_cards:
            print(card.id)
            if card.id == first_card.id:
                first_card_found_in_day_10 = True
        self.assertTrue(first_card_found_in_day_10)


if __name__ == '__main__':
    unittest.main()
