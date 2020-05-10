# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

import random

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    @property
    def rank(self):
        return self.card[0]

    @property
    def suit(self):
        return self.card[1]

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()


class PKCard(Card):
    """Card for Poker game
    """
    VALUES = dict(zip(ranks, range(2, 2+len(ranks))))

    def value(self):
        return PKCard.VALUES[self.card[0]]


class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.cards = [cls(r+s) for r in ranks for s in suits]

    def pop(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def __str__(self):
        return str(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)