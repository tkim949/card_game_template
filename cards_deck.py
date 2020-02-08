from os import path


class DeckOfCards:
    """
    todo: write docstring
    """
    def __init__(self, imgs_path, ace_high, deck_count, joker_count, joker_value=0):
        # cards is a dictionary of tuples --> {card: (path, value)}
        self.cards = {}
        for i in range(joker_count):
            suit = 'j'  # jokers will be referenced as j1, j2...
            self.cards[suit + str(i+1)] = (path.join(imgs_path, suit + str(i+1) + '.png'), joker_value)

        for suit in ['c','d','h','s']:
            for rank in range(1, 14):
                # each card is tuple(path, value). todo: custom values
                if rank == 1 and ace_high == True:
                    self.cards[suit + str(rank)] = (path.join(imgs_path, suit + str(rank) + '.png'), 14)
                else:
                    self.cards[suit + str(rank)] = (path.join(imgs_path, suit + str(rank) + '.png'), rank)

    def shuffled_deck(self):
        """

        :return: list: shuffled deck(s) of cards
        """
        pass


# ### TESTING ###
if __name__ == '__main__':
    # using current dir path
    tester = DeckOfCards(path.dirname(path.abspath(__file__)), True, 1, 1)
    for i in tester.cards:
        print(i,': ',tester.cards[i][0], tester.cards[i][1])

    print(type(tester.cards['j1']))
