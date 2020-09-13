import sys
import pygame


class Rocket:
    def __init__(self):
        pygame.init()
        size = width, height = (800, 600)
        self.screen = pygame.display.set_mode(size)
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(
            '/home/ericnguyen/Python/Python Crash Course/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        pygame.display.set_caption("Rocket in Center")
        self.rect.center = self.screen_rect.center
        self.BACKGROUND_COLOR = (230, 230, 230)
        # Movement of the Rocket
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rocket_speed = 1.5
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        # Initialize bullet characteristics
        self.bullet_speed = 0.8
        self.bullet_height = 10
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_rect = pygame.Rect(
            0, 0, self.bullet_width, self.bullet_height)
        self.bullet_pos = float(self.bullet_rect.y)
        self.bullets = pygame.sprite.Group()

    def rungame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
            self.rocket_move()
            self.bullet_move()
            self.update_screen()

    def _check_keydown(self, event):
        if event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def rocket_move(self):
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.rocket_speed
        elif self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.rocket_speed
        elif self.moving_up and (self.rect.top > self.screen_rect.top):
            self.y -= self.rocket_speed
        elif self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def bullet_move(self):
        self.bullet_pos += self.bullet_speed
        self.bullet_rect.y = self.bullet_pos

    def fire_bullet(self):
        if

    def update_screen(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        self.screen.blit(self.image, self.rect)
        for bullet in bullets.sprite():
            pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)
        pygame.display.flip()


if __name__ == '__main__':
    test = Rocket()
    test.rungame()
