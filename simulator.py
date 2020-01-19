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

    def simulate(self, days_amount):
        for i in range(days_amount):
            self.learn(i)
        self.print_cards()

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
            if card.learn_progress > 3:
                # do nothing, the reference will be cleared at the end of the for loop
                continue
            if card.learn_progress in self.learn_rhythm:
                try:
                    next_learning_day = current_day + self.learn_rhythm[card.learn_progress]
                    self.days[next_learning_day].append(card)
                except IndexError:
                    print('not enough calendar places initialized')
        self.days[current_day].clear()

    def get_cards_count(self):
        return sum([len(daily_cards)for daily_cards in self.days])

    def print_cards(self):
        for i, day in enumerate(self.days):
            print('day ' + str(i))
            for card in day:
                print(card.id)


class Card:

    def __init__(self):
        self.id = id(self)
        self.learn_progress = 0


if __name__ == '__main__':
    simulator = Simulator(365)
    simulator.simulate(days_amount=100)