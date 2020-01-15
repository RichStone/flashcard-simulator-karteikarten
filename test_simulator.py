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
        cards = simulator.get_cards(day=1)
        self.assertEqual(len(cards), 1)

    def test_simulator_has_365_cards_on_init(self):
        simulator = Simulator(card_amount=365)
        for cards in simulator.days:
            self.assertEqual(len(cards), 1)
        self.assertEqual(len(simulator.days), 365)

    def test_learned_first_day_card_appears_in_3_days(self):
        simulator = Simulator(card_amount=10)
        first_card = simulator.get_cards(day=1)[0]
        simulator.learn(day=1)
        day_3_cards = simulator.get_cards(day=3)
        first_card_found_in_day_3 = False
        for card in day_3_cards:
            if card.id == first_card.id:
                first_card_found_in_day_3 = True
        self.assertTrue(first_card_found_in_day_3)

    def test_learned_first_day_card_appears_on_day_10_after_2_learns(self):
        simulator = Simulator(card_amount=15)
        first_card = simulator.get_cards(day=1)[0]
        simulator.learn(day=1)
        simulator.learn(day=3)
        day_10_cards = simulator.get_cards(day=10)
        first_card_found_in_day_10 = False
        # TODO: Tests hang in and no implementation yet
        for card in day_10_cards:
            if card.id == first_card.id:
                first_card_found_in_day_10 = True
        self.assertTrue(first_card_found_in_day_10)

    # test_learned_first_day_card_doesnt_appear_anywhere_but_day_3(self):
    #   pass

    # def test_simulator_finds_failed_card_next_day(self):
    #     card = Card()
    #     Simulator.forgot(card)
    #     todays_cards = Simulator.get_cards()
    #     # ...?
    #     self.assertEqual()


if __name__ == '__main__':
    unittest.main()
