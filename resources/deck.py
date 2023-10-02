import random

from resources.card import Suit, CardValue, Card


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in Suit:
            for value in CardValue:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(self.cards)

    def __iter__(self):
        return iter(self.cards)
