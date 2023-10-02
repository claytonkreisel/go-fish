import os
from enum import Enum
import pygame
from .spritesheet import SpriteSheet
from config import ASSETS_DIR


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        ss = SpriteSheet(os.path.join(ASSETS_DIR, "cards-sprite.png"))
        self.image = ss.image_at(
            (
                (value.value - 1) * 71,
                (suit.value - 1) * 96,
                71,
                96,
            ),
        )
        self.rect = pygame.Rect(0, 0, 71, 96)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def __str__(self):
        return str(self.value.name) + " of " + str(self.suit.name)

    def __repr__(self):
        return str(self.value.name) + " of " + str(self.suit.name)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)
