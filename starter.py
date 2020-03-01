from cards_deck import *
import pygame
import random
from pathlib import Path
from os import path
from pygame.locals import*
import time
from pygame import mixer
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
'''
This is for music!
https://www.youtube.com/watch?v=4_9twnEduFA&t=314s
https://www.zamzar.com/
https://www.bensound.com/royalty-free-music/corporate-pop/3
Bfxr.com
https://online-audio-converter.com/
'''
class buttonM():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        #self.choose = choose

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 60)
            textSurf, textRect = makeText(self.text, font)
            #text = font.render(self.text, 1, (0, 0, 0))
            #screen.blit(textSurf, (self.x + (self.width / 2 - textSurf.get_width() / 2),
            #                       self.y + (self.height / 2 - textSurf.get_height() / 2)))
            textRect.move_ip(self.x + (self.width / 2 - textSurf.get_width() / 2),
                             self.y + (self.height / 2 - textSurf.get_height() / 2))
            screen.blit(textSurf, textRect)

    def isClick(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        #mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            self.color = BLUE
            return True

        return False


choose = 0
def music_choose():
    run = True
    music1 = buttonM((GREENDARK), 150, 100, 250, 100, 'Adventure')
    music2 = buttonM((GREENDARK), 150, 250, 250, 100, 'Energy')
    music3 = buttonM((GREENDARK), 150, 400, 250, 100, 'Perception')

    while run:
        global choose
        screen.fill(GREEN)
        dictText1 = pygame.font.SysFont("comicsansms", 40)
        Textsurf, Textrect = makeText("Choose Your Music!", dictText1)
        Textrect.move_ip(150, 50)
        screen.blit(Textsurf, Textrect)
        music1.draw(screen, BLACK)
        music2.draw(screen, BLACK)
        music3.draw(screen, BLACK)
        pygame.display.update()

        for event in pygame.event.get():
            mouse1 = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if music1.isClick(mouse1):
                    choose = 1
                elif music2.isClick(mouse1):
                    choose = 2
                elif music3.isClick(mouse1):
                    choose = 3
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music1.isClick(mouse1) or music2.isClick(mouse1) or music3.isClick(mouse1):
                    if music1.isClick(mouse1):
                        music1.color = BLUE
                    elif music2.isClick(mouse1):
                        music2.color = BLUE
                    elif music3.isClick(mouse1):
                        music3.color = BLUE
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music1.isClick(mouse1) or music2.isClick(mouse1) or music3.isClick(mouse1):
                    pickSound = mixer.Sound("Pickup_Coin100.wav")
                    pickSound.play()
                    card_choose()


# Refactoring from card_choose() and now I can use this for other texts also!!!
def makeText(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

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
        TextSurf, TextRect = makeText("Choose Your Card!", dictText)
        #TextSurf = dictText.render("Choose Your Card!", True, BLACK)
        #TextRect = TextSurf.get_rect()
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
    pickSound = mixer.Sound("Blip_Select72.wav")
    pickSound.play()
    createDeck(adeck)

# for the path to the classic card
def path2():
    adeck = DeckOfCards(path.join(path.dirname(path.abspath(__file__)), 'Cards/cardN'), True)
    pickSound = mixer.Sound("Blip_Select72.wav")
    pickSound.play()
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

            if choose == 1:
                mixer.music.load('bensound-adventure.wav')
            elif choose == 2:
                mixer.music.load('bensound-energy.wav')
            elif choose == 3:
                mixer.music.load('bensound-perception.wav')
            else:
                mixer.music.load('bensound-sweet.wav')
            mixer.music.play(-1)

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
music_choose()
# card_choose()
#play()
pygame.quit()
quit()
