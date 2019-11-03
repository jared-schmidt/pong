"""
Ball
"""

from random import randint
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    ''' Ball '''

    def __init__(self, point_x, point_y):
        super().__init__()

        self.color = BLACK
        self.width = 10
        self.height = 10
        self.direction = 'left'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, self.color, [
            0, 0, self.width, self.height])

        # self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()
        self.reset(point_x, point_y)

    def update(self):
        ''' update ball '''
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        ''' Ball hit other object '''
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def reset(self, point_x, point_y):
        ''' reset ball to screen '''
        self.rect.x = point_x
        self.rect.y = point_y
        self.velocity = [randint(4, 8), randint(-8, 8)]
