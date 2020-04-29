# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

########################## Class Card ##########################

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

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

########################## Class PKCard ##########################

class PKCard(Card):

    def value(self):  # Overriding
        if self.card[0] == '2': return 2
        if self.card[0] == '3': return 3
        if self.card[0] == '4': return 4
        if self.card[0] == '5': return 5
        if self.card[0] == '6': return 6
        if self.card[0] == '7': return 7
        if self.card[0] == '8': return 8
        if self.card[0] == '9': return 9
        if self.card[0] == 'T': return 10
        if self.card[0] == 'J': return 11
        if self.card[0] == 'Q': return 12
        if self.card[0] == 'K': return 13
        if self.card[0] == 'A': return 14


########################## Function main ##########################
'''
if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')

    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)
'''
########################## Class Deck ##########################

import random

class Deck:

    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = []
        for i in ranks:
            for j in suits:
                self.deck.append(PKCard(i+j))

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()
    
    def __str__(self):
        return f'{PKCard}'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self,index):
        return self.deck[index]

########################## Function main ##########################
'''
if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck.deck)
    # testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)
'''
########################## Class Hands ##########################

import collections

class Hands:

    def __init__(self, cards, players):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)
        self.players = players
        self.temp = []

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return len(self.cards)
    
    def cut_rank_only(self,l1,l2):
        for i in l1:
            l2.append(i[0])
    
    def cut_suit_only(self,l1,l2):
        for i in l1:
            l2.append(i[1])

    def change_rank_to_number(self,l1,l2):
        while(True):                      # clean the container
            if len(l2) == 0: break
            l2.pop()
        for i in l1:
            if i == '2': l2.append(2)
            if i == '3': l2.append(3)
            if i == '4': l2.append(4)
            if i == '5': l2.append(5)
            if i == '6': l2.append(6)
            if i == '7': l2.append(7)
            if i == '8': l2.append(8)
            if i == '9': l2.append(9)
            if i == 'T': l2.append(10)
            if i == 'J': l2.append(11)
            if i == 'Q': l2.append(12)
            if i == 'K': l2.append(13)
            if i == 'A': l2.append(14)
        
    def change_number_to_rank(self,l1,l2):
        while(True):                      # clean the container
            if len(l2) == 0: break
            l2.pop()
        for i in l1:
            if i == 2: l2.append('2')
            if i == 3: l2.append('3')
            if i == 4: l2.append('4')
            if i == 5: l2.append('5')
            if i == 6: l2.append('6')
            if i == 7: l2.append('7')
            if i == 8: l2.append('8')
            if i == 9: l2.append('9')
            if i == 10: l2.append('T')
            if i == 11: l2.append('J')
            if i == 12: l2.append('Q')
            if i == 13: l2.append('K')
            if i == 14: l2.append('A')

    def is_one_pair(self):
        temp_rank = []
        self.cut_rank_only(self.cards,temp_rank)
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 4: return True
        else: return False
    
    def is_two_pair(self):
        temp_rank = []
        self.cut_rank_only(self.cards,temp_rank)
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 3: return True
        else: return False
    
    def is_triple(self):
        temp_rank = []
        self.cut_rank_only(self.cards,temp_rank)
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if 3 in pair_dict.values(): return True
        else: return False

    def is_fourcard(self):
        temp_rank = []
        self.cut_rank_only(self.cards,temp_rank)
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 2: return True
        else: return False

    def is_straight(self):
        temp_rank1 = []
        self.cut_rank_only(self.cards,temp_rank1)
        temp_rank2 = []
        self.change_rank_to_number(temp_rank1,temp_rank2)
        sorted(temp_rank2)
        if temp_rank2[0]+2 == temp_rank2[1]+1 == temp_rank2[2] == temp_rank2[3]-1 == temp_rank2[4]-2: return True
        else: return False

    def is_flush(self):
        temp_suit = []
        self.cut_suit_only(self.cards,temp_suit)
        if temp_suit[0] == temp_suit[1] == temp_suit[2] == temp_suit[3] ==temp_suit[4]: return True
        else: return False

    def hand_ranking(self): # What's your rank?
        if self.is_straight() == True and self.is_flush() == True:       return 1   # Straight flush (Rank 1)
        elif self.is_fourcard() == True:                                 return 2   # Four of a kind (Rank 2)
        elif self.is_triple() == True and self.is_one_pair == True:      return 3   # Full house (Rank 3)
        elif self.is_flush() == True:                                    return 4   # Flush (Rank 4)
        elif self.is_straight() == True:                                 return 5   # Straight (Rank 5)
        elif self.is_triple() == True:                                   return 6   # Three of a kind (Rank 6)
        elif self.is_two_pair() == True:                                 return 7   # Two pair (Rank 7)
        elif self.is_one_pair() == True:                                 return 8   # One pair (Rank 8)
        else:                                                            return 9   # High card (Rank 9)

    def rank_value(self):
        return (self.hand_ranking(),self.cards)
    
    def match(self,other):
        if self.rank_value()[0] < other.rank_value()[0]: print(f'Player {self.players} Win!')
        if self.rank_value()[0] > other.rank_value()[0]: print(f'Player {other.players} Win!')
        if self.rank_value()[0] == other.rank_value()[0]:
            temp_rank1, temp_rank2 = [], []
            self.cut_rank_only(self.cards,temp_rank1)
            other.cut_rank_only(other.cards,temp_rank2)
            temp_rank3, temp_rank4 = [], []
            self.change_rank_to_number(temp_rank1,temp_rank3)
            other.change_rank_to_number(temp_rank2,temp_rank4)
            for i in range(len(temp_rank3)):
                if temp_rank3[i] > temp_rank4[i]: print(f'Player {self.players} Win!'); break
                if temp_rank3[i] < temp_rank4[i]: print(f'Player {other.players} Win!'); break

                

########################## Function main ##########################

if __name__ == '__main__':

    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)
    
    # test case1
    a_player_deck = Hands(['2C','5H','QD','QS','TH'],'A')
    b_player_deck = Hands(['3D','4C','4S','3H','3C'],'B')
    print(a_player_deck.rank_value())
    print(b_player_deck.rank_value())
    a_player_deck.match(b_player_deck)
    # test case 2
    a_player_deck = Hands(['4C','4H','4D','4S','TH'],'A')
    b_player_deck = Hands(['3H','3C','3D','3S','9C'],'B')
    print(a_player_deck.rank_value())
    print(b_player_deck.rank_value())
    a_player_deck.match(b_player_deck)
    # test case 3
    a_player_deck = Hands(['2C','2H','4D','4S','TH'],'A')
    b_player_deck = Hands(['JH','JC','9D','3S','3C'],'B')
    print(a_player_deck.rank_value())
    print(b_player_deck.rank_value())
    a_player_deck.match(b_player_deck)
    # test case 4
    a_player_deck = Hands(['3C','3H','3D','9S','TH'],'A')
    b_player_deck = Hands(['JH','JC','JD','3S','2C'],'B')
    print(a_player_deck.rank_value())
    print(b_player_deck.rank_value())
    a_player_deck.match(b_player_deck)