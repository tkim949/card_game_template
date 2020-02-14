from cards_deck import *
import pygame
import random
from pathlib import Path
from os import path
from pygame.locals import*
import time
img_dir = path.join(path.dirname(__file__), 'Cards')


"""
Skeleton for a new pygame
"""


SIZE = WIDTH, HEIGHT = 800, 600
FPS = 5
GREEN = 70, 120, 70
RED = (255, 0, 0)
GREENDARK = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


# initialize game and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Card Game')
clock = pygame.time.Clock()
'''
https://pythonprogramming.net/
https://kidscancode.org/
https://www.pygame.org/docs/ref/mouse.html
https://www.programcreek.com/python/example/6517/pygame.MOUSEBUTTONDOWN
'''
# show users card sample and prompt users to choose one.
modernImg = pygame.image.load("Cards/cardO/h13.png").convert()
classicImg = pygame.image.load("Cards/cardN/h13.png").convert()

# use mouse and click!
def button(x_cood, y_cood, wdt, height, colO, colC, action=None):
    #global cardImgP
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_cood + wdt > mouse[0] > x_cood and y_cood + height > mouse[1] > y_cood:
        pygame.draw.rect(screen, colC, (x_cood, y_cood, wdt, height))
        if click[0] == 1 and action != None:

            action()

    else:
        pygame.draw.rect(screen, colO, (x_cood, y_cood, wdt, height))

# show message and show button for user to click
def card_choose():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(GREEN)

        dictText = pygame.font.SysFont("comicsansms", 70)
        TextSurf = dictText.render("Choose Your Card!", True, BLACK)
        TextRect = TextSurf.get_rect()
        TextRect.move_ip(150, 100)
        screen.blit(TextSurf, TextRect)
        screen.blit(modernImg, (150, 200))
        screen.blit(classicImg, (500, 200))

        button(190, 430, 50, 50, GREENDARK, BLUE, path1)
        button(545, 430, 50, 50, GREENDARK, BLUE, path2)

        pygame.display.update()
        clock.tick(15)

# for the path to the modern card
def path1():
    adeck = DeckOfCards(path.join(path.dirname(path.abspath(__file__)), 'Cards/cardO'), True)
    createDeck(adeck)

# for the path to the classic card
def path2():
    adeck = DeckOfCards(path.join(path.dirname(path.abspath(__file__)), 'Cards/cardN'), True)
    createDeck(adeck)

cards = []
# create deck. you can change the number of cards by changing the range.
def createDeck(adeck):
    adeck = adeck.shuffled_deck()
    # card_j = adeck[0].get_img()
    for c in range(0, 5):
        cards.append(pygame.transform.scale(adeck[c].get_img(), (105, 143)))
    #cards.append(pygame.transform.scale(adeck[1].get_img(), (105, 143)))
    #cards.append(pygame.transform.scale(adeck[2].get_img(), (105, 143)))

    play()

    return adeck

# ## Game Loop ##
# puts the previous code into a function play()
def play():
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

        for c in range(0, 5):
            screen.blit(cards[c], (50 + 25*c, 407))
        #screen.blit(cards[1], (75, 407))
        #screen.blit(cards[2], (100, 407))
        # after rendering everything, flip. must b done last. double buffering
        pygame.display.flip()
        clock.tick(60)

#pygame.quit()
card_choose()
#play()
pygame.quit()
quit()
