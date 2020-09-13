import pygame

import sys


class Mario:
    def __init__(self, test_game):
        self.screen = test_game.screen
        self.screen_rect = test_game.screen.get_rect()
        self.image = pygame.image.load(
            '/home/ericnguyen/Python/Python Crash Course/alien_invasion/images/mario.bmp').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw_mario(self):
        self.screen.blit(self.image, self.rect)


class BlueSky:
    def __init__(self):
        pygame.init()
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode(
            (1200, 800))
        pygame.display.set_caption("Blue Sky")
        self.mario = Mario(self)

    def testrun(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move ship to the right
                        self.ship.rect.x += 1
            self.screen.fill(self.bg_color)
            self.mario.draw_mario()
            pygame.display.flip()


if __name__ == '__main__':
    ai = BlueSky()
    ai.testrun()
