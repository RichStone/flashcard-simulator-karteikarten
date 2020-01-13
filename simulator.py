class Simulator:
    def __init__(self):
        pass

    def simulate(self):
        pass

    @staticmethod
    def learn(card):
        card.learn_success = 2


class Card:
    def __init__(self):
        self.learn_success = 0
