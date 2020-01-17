from uuid import uuid1


class Simulator:
    def __init__(self, card_amount):
        # days is the 'calendar'
        # it's a list of lists filled with one new Card per day to learn
        self.days = [[Card()] for _ in range(card_amount)]
        self.learn_rhythm = {
            0: 1,
            1: 3,
            2: 7,
            3: 30,
        }

    def simulate(self):
        pass

    @staticmethod
    def learned(card):
        card.learn_progress += 1

    @staticmethod
    def forgot(card):
        card.learn_progress = 0

    def get_cards(self, day_idx):
        return self.days[day_idx]

    def learn(self, current_day):
        cards = self.get_cards(current_day)
        for card in cards:
            Simulator.learned(card)
            if card.learn_progress in self.learn_rhythm:
                try:
                    next_learning_day = current_day + self.learn_rhythm[card.learn_progress]
                    self.days[next_learning_day].append(card)
                except IndexError:
                    print('not enough calendar places initialized')

    def print_cards(self):
        for i, day in enumerate(self.days):
            print('day ' + str(i + 1))
            for card in day:
                print(card.id)

class Card:
    def __init__(self):
        self.id = uuid1()
        self.learn_progress = 0
