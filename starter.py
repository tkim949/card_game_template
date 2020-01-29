"""
Skeleton for a new pygame
"""

import pygame
import random

SIZE = WIDTH, HEIGHT = 320, 240
FPS = 30
GREEN = 0, 255, 0

# initialize game and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Card Game')
clock = pygame.time.Clock()

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
    # after rendering everything, flip. must b done last. double buffering
    pygame.display.flip()

pygame.quit()
