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

    def get_cards(self, day):
        return self.days[day - 1]

    def learn(self, day):
        cards = self.get_cards(day)
        for card in cards:
            self.days[2].append(card)


class Card:
    def __init__(self):
        self.id = uuid1
        self.learn_progress = 0
