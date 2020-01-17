from uuid import uuid1


class Simulator:
    def __init__(self, card_amount):
        # days is the 'calendar'
        # it's a list of lists filled with cards to learn
        self.days = [[Card()] for _ in range(card_amount)]

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

    def learn(self, day):
        cards = self.get_cards(day)
        for card in cards:
            if card.learn_progress == 0:
                try:
                    self.days[day + 3].append(card)
                except IndexError:
                    print('not enough calendar places initialized')
            if card.learn_progress == 1:
                try:
                    if self.days[day + 7]:
                        self.days[day + 7].append(card)
                except IndexError:
                    print('not enough calendar places initialized')
            Simulator.learned(card)

    def print_cards(self):
        for i, day in enumerate(self.days):
            print('day ' + str(i + 1))
            for card in day:
                print(card.id)

class Card:
    def __init__(self):
        self.id = uuid1()
        self.learn_progress = 0
