class Simulator:
    def __init__(self):
        pass

    def simulate(self):
        pass

    @staticmethod
    def learned(card):
        card.learn_progress += 1


class Card:
    def __init__(self):
        self.learn_progress = 0
