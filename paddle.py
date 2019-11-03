"""
Paddle
"""

import pygame

WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
WIDTH = 5
HEIGHT = 70
SPEED = 50

class Paddle(pygame.sprite.Sprite):
    ''' Paddle '''

    def __init__(self):
        super().__init__()

        self.color = BLUE
        self.width = WIDTH
        self.height = HEIGHT
        self.speed = SPEED

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, self.color, [
            0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        ''' Moves paddle up '''
        self.rect.y -= pixels

    def move_down(self, pixels):
        ''' Moves paddle down '''
        self.rect.y += pixels
