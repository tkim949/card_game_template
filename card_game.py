import pygame
from pygame import mixer
import os
# from os import path
from cards_deck import *

'''
Sources:
https://pythonprogramming.net/
https://kidscancode.org/
https://www.pygame.org/docs/ref/mouse.html
https://www.programcreek.com/python/example/6517/pygame.MOUSEBUTTONDOWN
'''

"""
project scope variables
"""
__file__ = os.path.abspath(__file__)
SIZE = WIDTH, HEIGHT = 800, 600
FPS = 10
GREENDARK = (0, 255, 0)
# BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 210, 28)
BLUE = (173, 216, 230)
RED = (255, 144, 144)

# set paths to game folder / directory
game_path = os.path.dirname(__file__)
# direct 'backgrounds' folder path
bkg_path = os.path.join(game_path, "backgrounds")
menu_path = os.path.join(game_path, "menu")

# initialize and create window
pygame.init()
pygame.mixer.init()  # sound stuff
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Awesome Card Game")
clock = pygame.time.Clock()

# show users card sample and prompt users to choose one.
modernImg = pygame.image.load("Cards/cardO/h13.png").convert()
classicImg = pygame.image.load("Cards/cardN/h13.png").convert()

"""
SECTION A: Menu
"""
solid_color_choice = WHITE
background_image_choice = False

# Font definitions
font_size = 36
font_color = BLACK
font_color_selected = BLUE


# Game states
#	Menu
#		Playing
#			Pick Game (load)
#			Play Game (from chosen)
#			Pick Music
#			Quit
#		Development
#			New Game
#			Load Game
#	Win
#	Lose
#	Undo
#	AI Stuff (i.e. player 2)
#	Quit
#	High Score

def read_menu_file(menu_file):
    # load menu choices
    if (type(menu_file) == str):
        f = open(menu_file)
        menu_lines = f.readlines()
        f.close
        return menu_lines
    else:
        return menu_file


# Game Menu
def display_menu(menu_file):
    global solid_color_choice
    menu_on = True

    menu_lines = read_menu_file(menu_file)
    menu_choices = len(menu_lines)
    selected_menu_choice = 1

    # Actual text of menu item
    font = pygame.font.Font("VertigoFLF.ttf", font_size)
    menuTextSurf = font.render("menu display", True, font_color)
    menuTextRect = menuTextSurf.get_rect()

    # make loop
    # print("running menu")
    while menu_on:
        for event in pygame.event.get():
            # Quit option
            if event.type == pygame.QUIT:
                quit()

            # Options to go up or down in menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_menu_choice += 1
                if event.key == pygame.K_UP:
                    selected_menu_choice -= 1
                if event.key == pygame.K_RETURN:
                    return selected_menu_choice

        # Ensure menu choice is not out of bounds
        selected_menu_choice = max(1, selected_menu_choice)
        selected_menu_choice = min(menu_choices, selected_menu_choice)

        # Display menu background
        set_game_background()

        # Setup location and display text of menu items
        menuTextRect.centerx = int(WIDTH / 3)
        menuTextRect.centery = int(HEIGHT / 4)

        for i in menu_lines:
            # display each line 1 lower than previous
            menuTextRect.centery += font_size
            # each i has a newline character that needs to be removed
            # change color if menu choice selected
            if (int(i[0:1]) == selected_menu_choice):
                menuTextSurf = font.render(i[:-1], True, font_color_selected)
            else:
                menuTextSurf = font.render(i[:-1], True, font_color)

            # Updates to screen display
            # TODO: do we need this to be within for loop
            screen.blit(menuTextSurf, menuTextRect)

        pygame.display.flip()
        clock.tick(FPS)

    # Menu Reaction to key strokes


def set_background_solid():
    global solid_color_choice
    # hardcode menu choices
    # 1. White (default)
    # 2. Green
    # 3. Blue
    # 4. Red
    solid_background_choice = display_menu(os.path.join(menu_path, "background_solid_choices.txt"))

    if (solid_background_choice == 1):
        solid_color_choice = WHITE
    elif (solid_background_choice == 2):
        solid_color_choice = GREEN
    elif (solid_background_choice == 3):
        solid_color_choice = BLUE
    elif (solid_background_choice == 4):
        solid_color_choice = RED

    # TODO: doublecheck WHITE functionality

    screen.fill(solid_color_choice)
    pygame.display.update()


def set_background_artwork():
    global background_image_choice
    global solid_color_choice
    # hardcode menu choices
    # 1. Cave
    # 2. Space
    # 3. Viking
    artwork_background_choice = display_menu(os.path.join(menu_path, "background_artwork_choices.txt"))

    if (artwork_background_choice == 1):
        # if the choice is campfire
        background_image_choice = pygame.image.load(os.path.join(bkg_path, "campfire.png")).convert()
    elif (artwork_background_choice == 2):
        # if the choice is space
        background_image_choice = pygame.image.load(os.path.join(bkg_path, "space.jpg")).convert()
    elif (artwork_background_choice == 3):
        # if the choice is vikings
        background_image_choice = pygame.image.load(os.path.join(bkg_path, "vikings.png")).convert()

    print(background_image_choice)

    solid_color_choice = False
    screen.blit(background_image_choice, [0, 0])
    pygame.display.flip()


def set_game_background():
    global solid_color_choice
    global background_image_choice
    global font_color
    global font_color_selected

    if (solid_color_choice != False):
        screen.fill(solid_color_choice)
        background_image_choice = False
    else:
        screen.blit(background_image_choice, [0, 0])
        solid_color_choice = False

    if (solid_color_choice == WHITE):
        font_color = BLACK
        font_color_selected = BLUE
    else:
        font_color = BLACK
        font_color_selected = WHITE


"""
SECTION B: Music
"""
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
        # self.choose = choose

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 60)
            textSurf, textRect = makeText(self.text, font)
            # text = font.render(self.text, 1, (0, 0, 0))
            # screen.blit(textSurf, (self.x + (self.width / 2 - textSurf.get_width() / 2),
            #                       self.y + (self.height / 2 - textSurf.get_height() / 2)))
            textRect.move_ip(self.x + (self.width / 2 - textSurf.get_width() / 2),
                             self.y + (self.height / 2 - textSurf.get_height() / 2))
            screen.blit(textSurf, textRect)

    def isClick(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        # mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()
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
                # pygame.quit()
                # quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if music1.isClick(mouse1):
                    mixer.music.load('bensound-adventure.wav')
                    # choose = 1
                elif music2.isClick(mouse1):
                    mixer.music.load('bensound-energy.wav')
                    # choose = 2
                elif music3.isClick(mouse1):
                    mixer.music.load('bensound-perception.wav')
                    # choose = 3
                else:
                    mixer.music.load('bensound-sweet.wav')
                mixer.music.play(-1)
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
                    # card_choose()
                    run = False


"""
SECTION C: Card layout
"""


# Refactoring from card_choose() and now I can use this for other texts also!!!
def makeText(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# use mouse and click!
def button(x_cood, y_cood, wdt, height, colO, colC, action=None):
    # global cardImgP
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
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(GREEN)

        dictText = pygame.font.SysFont("comicsansms", 70)
        TextSurf, TextRect = makeText("Choose Your Card!", dictText)
        # TextSurf = dictText.render("Choose Your Card!", True, BLACK)
        # TextRect = TextSurf.get_rect()
        TextRect.move_ip(150, 100)
        screen.blit(TextSurf, TextRect)
        screen.blit(modernImg, (150, 200))
        screen.blit(classicImg, (500, 200))

        button(190, 430, 50, 50, GREENDARK, BLUE, path1)
        button(545, 430, 50, 50, GREENDARK, BLUE, path2)

        pygame.display.update()
        clock.tick(FPS)


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
    # cards.append(pygame.transform.scale(adeck[1].get_img(), (105, 143)))
    # cards.append(pygame.transform.scale(adeck[2].get_img(), (105, 143)))

    play()  # starts the game
    return adeck


def play():
    """
     ### GAME LOOP ###
     this will run after the play game option has been chosen from the main menu
     pressing the close window button brings it back to main screen
    """
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
            screen.blit(cards[c], (50 + 25 * c, 407))
        # screen.blit(cards[1], (75, 407))
        # screen.blit(cards[2], (100, 407))
        # after rendering everything, flip. must b done last. double buffering
        pygame.display.flip()
        clock.tick(FPS)


running = True
while running:
    # Display menu
    clock.tick(FPS)
    game_state = display_menu(os.path.join(menu_path, "menu.txt"))

    # Games States - MUST align with what is in "menu.txt"
    #	1. Choose Game
    #	2. Play Game
    #	3. Choose Background
    #	4. Pick Music (placeholder)
    #	5. Create new Game (placeholder)
    #	6. Load Game to Edit (placeholder)
    #	7. Quit

    # Switch/case on game states above
    if (game_state == 1):
        print("choosing new game")
    elif (game_state == 2):
        print("playing new game")
        card_choose()
    elif (game_state == 3):
        print("choosing background")
        background_choice = display_menu(os.path.join(menu_path, "background_menu.txt"))
        print(background_choice)
        if (background_choice == 1):
            set_background_solid()
        elif (background_choice == 2):
            set_background_artwork()
    elif (game_state == 4):
        print("picking music")
        music_choose()
    elif (game_state == 5):
        print("creating new game")
    elif (game_state == 5):
        print("loading game to edit")
    elif (game_state == 7):
        print("Quiting game")
        quit()

# Wait for input

quit()
# Game logic
# Win logic
# Lose logic
# menu logic

# Render

# Background color
# set_game_background()


# Refresh (after draw)
# pygame.display.flip()
