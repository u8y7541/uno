from random import shuffle
class Card:
    def __init__(self, rank, suite):
        self.rank, self.suite = rank, suite
    def __str__(self):
        return str(self.rank) + ' of ' + self.suite
    def __repr__(self):
        return str(self)
class Deck:
    def __init__(self, preset = -1):
        if preset == -1:
            self.cardsList = [[Card(i, j) for i in list(range(1, 10)) + \
                               ['Skip', 'Reverse', 'Draw Two']] for j in \
                              ['Red', 'Green', 'Blue', 'Yellow']] * 2 \
                              + [Card('WILD', 'WILD'), \
                                 Card('WILD', 'DRAW FOUR')] * 4 \
                                 + [Card(0, i) for i in ['Red', 'Green', \
                                                         'Blue', 'Yellow']]
            self.cardsList = (self.cardsList[0] + self.cardsList[1] + \
                              self.cardsList[2] + self.cardsList[3]) * 2 \
                              + self.cardsList[8:]
        else:
            self.cardsList = preset
    def shuffle(self):
        shuffle(self.cardsList)
    def draw(self):
        return self.cardsList.pop(0)
    def addCard(self, card):
        self.cardsList.append(card)
class Hand(Deck):
    def __init__(preset = []):
        super().__init__(preset)
class Heap(Hand):
    pass
class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name
    def play(self):
        pass
