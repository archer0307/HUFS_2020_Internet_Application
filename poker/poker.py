import sys
from enum import IntEnum
import logging
if sys.version_info < (3, 6):
    # Use OrderedDict, instead.
    from collections import OrderedDict as dict

from card import PKCard, Deck, ranks, suits

class Ranking(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class Hands:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        card_list = []
        for card in cards:
            if isinstance(card, PKCard):
                card_list.append(card)
            else:
                card_list.append(PKCard(card))
        self.cards = card_list
        self.ranking = None

    def __repr__(self):
        return '-'.join([repr(c) for c in self.cards]) + ': ' + repr(self.cards)
    
    def _check(self,other):
        if self.ranking is None or other.ranking is None:
            raise AttributeError('not evaluated. call eval() method')

    def __eq__(self, other):
        self._check(other)
        return (self.ranking, self.cards) == (other.ranking, other.cards)

    def __gt__(self,other):
        self._check(other)
        return (self.ranking, self.cards) > (other.ranking, other.cards)

    def __lt__(self,other):
        self._check(other)
        return (self.ranking, self.cards) < (other.ranking, other.cards)

    def __ne__(self,other): return not self.__eq__(other)
    def __le__(self,other): return not self.__gt__(other)
    def __ge__(self,other): return not self.__lt__(other)

    def is_flush(self):
        self.cards.sort(reverse=True)
        suited = dict((suit, 0) for suit in suits)
        for card in self.cards:
            suited[card.suit] += 1      # count for each suit
        return max(suited.values()) >= 5
    
    def is_straight(self):
        """Returns card list making straight or []

        Don't need to check straight flush.
        """
        self.cards.sort(reverse=True)
        values = [c.value() for c in self.cards]
        if values == list(range(values[0], values[0]-5, -1)):
            return True
        if values[0] == PKCard('AS').value():       # if Ace exists
            values.pop(0)
            values.append(1)        # use Ace as 1
            if values == list(range(values[0], values[0]-5, -1)):
                # re-arrange cards
                ace = self.cards.pop(0)
                self.cards.append(ace)
                return True
        return False

    def classify_by_rank(self):
        ranked = dict()
        for card in self.cards:
            if card.rank in ranked:
                ranked[card.rank].append(card)
            else:
                ranked[card.rank] = [card]
        return ranked

    def find_a_kind(self):
        self.cards.sort(reverse=True)
        ranked = self.classify_by_rank()
        # classify by number of cards of same rank
        kind = dict()
        for cards in ranked.values():
            l = len(cards)      # cards: list of PKCard instances of same card
            if l >= 2:          # pair, tripple, four
                if l in kind:
                    kind[l].append(cards)
                else:
                    kind[l] = [cards]

        ranking = None
        hand_cards = []
        if 4 in kind:
            hand_cards.extend(kind[4][0])
            ranking = Ranking.FOUR_OF_A_KIND
        elif 3 in kind:
            hand_cards.extend(kind[3][0])
            if 2 in kind:
                hand_cards.extend(kind[3][0])
                ranking = Ranking.FULL_HOUSE
            else:
                ranking = Ranking.THREE_OF_A_KIND
        elif 2 in kind:
            hand_cards.extend(kind[2][0])
            if len(kind[2]) > 1:
                hand_cards.extend(kind[2][1])
                ranking = Ranking.TWO_PAIRS
            else:
                ranking = Ranking.ONE_PAIR

        if ranking:
            kickers = [c for c in self.cards if c not in hand_cards]
            self.cards = hand_cards + kickers
        return ranking

    def eval(self):
        """Find the hand ranking.
        """
        flush = self.is_flush()
        if flush:
            if self.is_straight():
                self.ranking = Ranking.STRAIGHT_FLUSH
            else:
                self.ranking = Ranking.FLUSH
            return
        if self.is_straight():
            self.ranking = Ranking.STRAIGHT
        else:
            ranking = self.find_a_kind()
            self.ranking = ranking if ranking else Ranking.HIGH_CARD
