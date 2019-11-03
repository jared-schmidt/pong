"""
main
"""

import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 250

# colors
WHITE = (255, 255, 255)
GREEN = (20, 255, 140)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")

ALL_SPRITES_LIST = pygame.sprite.Group()

# Add player
PLAYER = Paddle()
PLAYER.rect.x = 20
PLAYER.rect.y = 50
ALL_SPRITES_LIST.add(PLAYER)

# Add ball
BALL = Ball(100, 100)
# BALL.rect.x = 100
# BALL.rect.y = 100
ALL_SPRITES_LIST.add(BALL)

SCORE = 0

RUNNING = True
CLOCK = pygame.time.Clock()

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                RUNNING = False

    # Key presses
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_UP] and PLAYER.rect.y >= 0:
        PLAYER.move_up(5)
    if KEYS[pygame.K_DOWN] and PLAYER.rect.y < SCREEN_HEIGHT - PLAYER.height:
        PLAYER.move_down(5)

    # game logic
    ALL_SPRITES_LIST.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if BALL.rect.x >= SCREEN_WIDTH - BALL.width:
        BALL.velocity[0] = -BALL.velocity[0]
    if BALL.rect.x <= 0:
        print("hit back wall")
        BALL.reset(100, 100)
        # BALL.velocity[0] = -BALL.velocity[0]
    if BALL.rect.y > SCREEN_HEIGHT - BALL.height:
        BALL.velocity[1] = -BALL.velocity[1]
    if BALL.rect.y < 0:
        BALL.velocity[1] = -BALL.velocity[1]

    if pygame.sprite.collide_mask(BALL, PLAYER):
        SCORE += 1
        BALL.bounce()

    SCREEN.fill(GREEN)

    ALL_SPRITES_LIST.draw(SCREEN)

    # display score
    FONT = pygame.font.Font(None, 74)
    TEXT = FONT.render(str(SCORE), 1, WHITE)
    SCREEN.blit(TEXT, (250, 10))

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
