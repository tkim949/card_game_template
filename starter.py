"""
Skeleton for a new pygame
"""

import pygame
import random

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 5
GREEN = 70, 120, 70

# initialize game and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Card Game')
ball = pygame.image.load("intro_ball.gif")
clock = pygame.time.Clock()
card_j = pygame.image.load("Cards/jk.png")
card = pygame.transform.scale(card_j, (105,143))

# ## Game Loop ##
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # A) Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # B) Update

    # C) Render
    screen.fill(GREEN)
    screen.blit(card, (50, 407))
    screen.blit(card, (70, 407))
    # after rendering everything, flip. must b done last. double buffering
    pygame.display.flip()

pygame.quit()
