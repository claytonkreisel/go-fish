import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from resources.card import Card, Suit, CardValue


class Game(object):
    def __init__(self):
        pass

    def run(self):
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)

        running = True
        while running:
            card = Card(Suit.SPADES, CardValue.ACE)
            card.draw(pygame.display.get_surface())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
