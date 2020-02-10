from cards_deck import *


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
clock = pygame.time.Clock()
adeck = DeckOfCards(path.join(path.dirname(path.abspath(__file__)), 'Cards'), True)
adeck = adeck.shuffled_deck()
# card_j = adeck[0].get_img()
card = pygame.transform.scale(adeck[0].get_img(), (105,143))
card1 = pygame.transform.scale(adeck[1].get_img(), (105,143))
card2 = pygame.transform.scale(adeck[2].get_img(), (105,143))

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
    screen.blit(card1, (75, 407))
    screen.blit(card2, (100, 407))
    # after rendering everything, flip. must b done last. double buffering
    pygame.display.flip()

pygame.quit()
