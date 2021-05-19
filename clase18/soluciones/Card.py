import random
import time

class Card:
    """ Clase que representa una carta de poker """

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Treboles', 'Corazones', 'Diamantes', 'Picas']
    rank_names = [None, 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Reina', 'Rey']

    def __str__(self):
        return '%s de %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        c1 = self.suit, self.rank
        c2 = other.suit, other.rank
        return c1 < c2

class Deck:
    """ Clase que representa una baraja de cartas inglesas """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        #self.cards = sorted(self.cards)
        self.cards.sort()

    def move_cards(self, hand, num=1):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, nhands, ncards):
        """ Regresa una lista de Hands de tamaño nhands con ncards cada una """
        res = []
        for i in range(nhands):
            hand = Hand()
            self.move_cards(hand, ncards)
            res.append(hand)
        return res

class Hand(Deck):
    def __init__(self, label=''):
        self.label = label
        self.cards = []

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    mi_mano = Hand('Mi mano')
    deck.move_cards(mi_mano, 5)

    print(mi_mano)

    mi_mano.move_cards(deck, 1)

    print('*'*10)
    print(mi_mano)

    otro = Hand('Otro')
    deck.move_cards(otro, 5)

    print('*'*10)
    print(otro)

    otro.move_cards(mi_mano, 1)

    print('*'*10)
    print(mi_mano)

    print('*'*10)
    manos = deck.deal_hands(3, 5)
    for mano in manos:
        print(mano)
        print('*'*10)
