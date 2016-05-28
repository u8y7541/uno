import base
from playerTypes import *

class Game:
    def __init__(self, playerNames, playerTypes, startingCards = 7):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [eval(playerTypes[i] + '(' + \
                             playerNames[i] \
                             + ')' for i in range(len(playerNames)))]
        for i in self.players:
            [i.hand.addCard(deck.draw()) for i in range(startingCards)]
        self.cardHeap = Heap()
    def play(self):
        while '0' not in [len(i.hand.cardsList) for i in self.players]:
            for i in self.players:
                self.cardHeap.append(i.play())
