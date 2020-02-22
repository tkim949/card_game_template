"""
Skeleton for a new pygame
"""

import pygame
import random


SIZE = WIDTH, HEIGHT = 800, 450
FPS = 30
GREEN = 153,255,204
LIGHT_GR = 204, 255, 229

# initialize game and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Card Game')
clock = pygame.time.Clock()


class Card:
    def __init__ (self, color, height, width, border):
        self.color = color
        self.height = height
        self.width = width
        self.border = border

    def get_color(self):
        return self.color

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_border(self):
        return self.border

    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width

class Hand:
    def __init__(self, num_cards, num_players, draw_pile, space_between):
        self.num_cards = num_cards
        self.num_players = num_players
        self.draw_pile = draw_pile
        self.space_between = space_between


    def deal(self):
        ## should take the size of the cards and size of the board, perform math and place them evenly along each edge
        card_top = 310
        card_left = 200
        count = 0

        ## Nested loop loops once for # of players and again for each card in hand
        ## The card's size and player number will dictate the card's spaceing via the nested if statement
        for x in range(0, self.num_players):
            print("player loop")
            count += 1
            for y in range(0, self.num_cards):
                pygame.draw.rect(screen, Card.get_color(card), (card_left, card_top, Card.get_width(card), Card.get_height(card)), Card.get_border(card))
                if count == 1 or count == 2:
                    if Card.get_width(card) < Card.get_height(card):
                        card_left += self.space_between
                    else:
                        card_top -= self.space_between
                else:
                    if Card.get_width(card) < Card.get_height(card):
                        card_left -= self.space_between
                    else:
                        card_top += self.space_between

                print("card loop")
            swap = Card.get_height(card)
            card.set_height(Card.get_width(card))
            card.set_width(swap)

card = Card((0,0,0), 105, 75, 3)
p1 = Hand(4, 4, 1, 85)
p1.deal()



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
    screen.fill(LIGHT_GR)
    pygame.draw.rect(screen, GREEN, (20, 20, 760, 410))
    pygame.draw.rect(screen, LIGHT_GR, (30, 30, 740, 390))
    p1.deal()

    # after rendering everything, flip. must b done last. double buffering
    pygame.display.flip()

"""
    # Player's Hand of Cards
    i=0
    hand_top = 310
    hand_left = 200
    cards_in_hand = 5
    while i < cards_in_hand:
        pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 75, 105), 3)
        hand_left += 85
        i+= 1

    # Oponent's Hands
    i=0
    hand_top = 30
    hand_left = 200
    cards_in_hand = 5
    while i < cards_in_hand:
        pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 75, 105), 3)
        hand_left += 85
        i+= 1

    # Right Side Oponent's Hands
    i=0
    hand_top = 360
    hand_left = 690
    cards_in_hand = 5
    while i < cards_in_hand:
        pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 105, 75), 3)
        hand_top -= 85
        i+= 1

    # Left Side Oponent's Hands
    i=0
    hand_top = 360
    hand_left = 30
    cards_in_hand = 5
    while i < cards_in_hand:
        pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 105, 75), 3)
        hand_top -= 85
        i+= 1


    # Draw Pile
    hand_top = 160
    hand_left = 300
    pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 75, 105), 3)

    # Played Cards
    hand_top = 160
    hand_left = 400
    pygame.draw.rect(screen, (0, 0, 0), (hand_left, hand_top, 75, 105), 3)
"""

## Kaylin is trying to properly connect github to pycharm

pygame.quit()
