import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from resources import Card, Suit, CardValue, Deck


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        self.deck = Deck()
        self.deck.shuffle()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        deck = self.deck
                        card = deck.draw()
                        card.draw(pygame.display.get_surface())

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
