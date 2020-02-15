from os import path
from pygame import image
import random


class Card:
    """
    To be used with the pygame template
    """

    def __init__(self, suit, rank, imgs_path=None):
        """

        :param suit: string or char to identify the suit
        :param rank: integer from 1 - 13 (ace = 1), or 2-14 (ace = 14)
        :param imgs_path: path of the top folder where cards are saved.
            [WARNING] card names must follow the convention: [suit:'h','c','d','s','j'=joker][rank: 1-13]
            ex: c1 = clubs Ace, j1 = joker 1
        """
        self.suit = suit
        self.rank = rank
        # set up path for card image
        if imgs_path is not None:
            if rank == 1 or rank == 14:  # set Ace
                self.img = image.load(path.join(imgs_path, suit + '1' + '.png'))
            else:
                self.img = image.load(path.join(imgs_path, suit + str(rank) + '.png'))

    def get_name(self):
        return self.suit + str(self.rank)

    def get_img(self):
        return self.img

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class DeckOfCards:
    """
    to be used with pygame template. Deck of cards only needs to be setup once per game.
    decks can then be retrieved as needed.
    """

    def __init__(self, imgs_path, ace_high=False, joker_count=0, joker_value=0):
        self.cards = []
        for i in range(joker_count):
            # j suit will be used for jokers, referenced as j1, j2...
            self.cards.append(Card('j', i, imgs_path, joker_value))

        for suit in ['c', 'd', 'h', 's']:
            for rank in range(1, 14):
                if rank == 1 and ace_high:
                    self.cards.append(Card(suit, 14, imgs_path))
                else:
                    self.cards.append(Card(suit, rank, imgs_path))

    def get_a_deck(self):
        return self.cards

    def shuffled_deck(self, count=1):
        """

        :param count: how many decks to return
        :return: list: shuffled deck(s) of cards
        """
        rtn = []
        for i in range(count):
            rtn.extend(random.sample(self.cards, len(self.cards)))

        return rtn

    # [sm] maybe this should be done at the game level, just use this class to create deck
    def deal_hand(self, qty):
        pass


# ### TESTING ###
if __name__ == '__main__':
    # using current dir path
    # tester = DeckOfCards(path.dirname(path.abspath(__file__)), True, 1, 1)
    # for i in tester.cards:
    #     print(i,': ',tester.cards[i][0], tester.cards[i][1])
    #
    # print(type(tester.cards['j1']))
    #
    # bunch = []
    # bunch.append(Card('s', 9, path.dirname(path.abspath(__file__))))
    # print(bunch[0].img)
    # # ace = Card('s',14,path.dirname(path.abspath(__file__)))
    # # print(ace.img)
    # # print(ace.rank)
    adeck = DeckOfCards(path.join(path.dirname(path.abspath(__file__)), 'Cards'), False)
    adeck = adeck.shuffled_deck()
    print(len(adeck))
    for crd in adeck:
        print(crd.get_name(), '|', crd.get_rank(), '|', crd.get_img())
