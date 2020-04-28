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
        # self.cards = sorted(cards, reverse=True)
        self.cards = cards
        self.players = players

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return len(self.cards)
    
    def high_card_in_145(self):
        temp_rank1 = []
        for i in self.cards:
            temp_rank1.append(i[0])
        temp_rank2 = []
        for i in temp_rank1:
            if i == '2': temp_rank2.append(2)
            if i == '3': temp_rank2.append(3)
            if i == '4': temp_rank2.append(4)
            if i == '5': temp_rank2.append(5)
            if i == '6': temp_rank2.append(6)
            if i == '7': temp_rank2.append(7)
            if i == '8': temp_rank2.append(8)
            if i == '9': temp_rank2.append(9)
            if i == 'T': temp_rank2.append(10)
            if i == 'J': temp_rank2.append(11)
            if i == 'Q': temp_rank2.append(12)
            if i == 'K': temp_rank2.append(13)
            if i == 'A': temp_rank2.append(14)
        return max(temp_rank2)
    
    def high_card_in_236(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        return max(pair_dict.keys(),key=pair_dict.get)

    def high_card_in_7(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)

        num = 0
        ret = []
        for i,j in sorted(pair_dict.items(), key =lambda x:x[1]):
            num += 1
            ret.append(i)
            if num >=2: break
        return ret
    
    def high_card_in_8(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)

        for i,j in sorted(pair_dict.items(), key =lambda x:x[1]):
            return i

    def is_one_pair(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 4: return True
        else: return False
    
    def is_two_pair(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 3: return True
        else: return False
    
    def is_triple(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if 3 in pair_dict.values(): return True
        else: return False

    def is_fourcard(self):
        temp_rank = []
        for i in self.cards:
            temp_rank.append(i[0])
        pair_dict = collections.Counter(temp_rank)  # Use dictionary to count pair
        if len(pair_dict) == 2: return True
        else: return False

    def is_straight(self):
        temp_rank1 = []
        for i in self.cards:
            temp_rank1.append(i[0])
        temp_rank2 = []
        for i in temp_rank1:
            if i == '2': temp_rank2.append(2)
            if i == '3': temp_rank2.append(3)
            if i == '4': temp_rank2.append(4)
            if i == '5': temp_rank2.append(5)
            if i == '6': temp_rank2.append(6)
            if i == '7': temp_rank2.append(7)
            if i == '8': temp_rank2.append(8)
            if i == '9': temp_rank2.append(9)
            if i == 'T': temp_rank2.append(10)
            if i == 'J': temp_rank2.append(11)
            if i == 'Q': temp_rank2.append(12)
            if i == 'K': temp_rank2.append(13)
            if i == 'A': temp_rank2.append(14)
        sorted(temp_rank2)
        if temp_rank2[0]+2 == temp_rank2[1]+1 == temp_rank2[2] == temp_rank2[3]-1 == temp_rank2[4]-2: return True
        else: return False

    def is_flush(self):
        temp_suit = []
        for i in self.cards:
            temp_suit.append(i[1])
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

    def value(self,value):
        if value == '2': return 2
        if value == '3': return 3
        if value == '4': return 4
        if value == '5': return 5
        if value == '6': return 6
        if value == '7': return 7
        if value == '8': return 8
        if value == '9': return 9
        if value == 'T': return 10
        if value == 'J': return 11
        if value == 'Q': return 12
        if value == 'K': return 13
        if value == 'A': return 14

    def match(self,other):  # Let's fight
        if value(self.hand_ranking()) > value(other.hand_ranking()): print(f'Player {self.players} Win!')
        if value(self.hand_ranking()) < value(other.hand_ranking()) : print(f'Player {other.players} Win!')
        if value(self.hand_ranking()) == value(other.hand_ranking()) :
            if value(self.hand_ranking()) == 1 or value(self.hand_ranking()) == 4 or value(self.hand_ranking()) == 5:                            # If ranks draw in Straight flush/Flush/Straight
                if value(self.high_card_in_145()) > value(other.high_card_in_145()): print(f'Player {self.players} Win!')
                if value(self.high_card_in_145()) < value(other.high_card_in_145()): print(f'Player {other.players} Win!')
                if value(self.high_card_in_145()) == value(other.high_card_in_145()): print('Draw!')
            if value(self.hand_ranking()) == 2 or value(self.hand_ranking()) == 3 or value(self.hand_ranking()) == 6:                            # If ranks draw in Four of a kind/Full house/Three of a kind
                if value(self.high_card_in_236()) > value(other.high_card_in_236()): print(f'Player {self.players} Win!')
                if value(self.high_card_in_236()) < value(other.high_card_in_236()): print(f'Player {other.players} Win!')
                if value(self.high_card_in_236()) == value(other.high_card_in_236()): print('Draw!')
            if value(self.hand_ranking()) == 7:                                                                                    # If ranks draw in Two pair
                if value(self.high_card_in_7()[0]) > value(other.high_card_in_7()[0]): print(f'Player {self.players} Win!')
                if value(self.high_card_in_7()[0]) < value(other.high_card_in_7()[0]): print(f'Player {other.players} Win!')
                if value(self.high_card_in_7()[0]) == value(other.high_card_in_7()[0]):
                    if value(self.high_card_in_7()[1]) > value(other.high_card_in_7()[1]): print(f'Player {self.players} Win!')
                    if value(self.high_card_in_7()[1]) < value(other.high_card_in_7()[1]): print(f'Player {other.players} Win!')
                    if value(self.high_card_in_7()[1]) == value(other.high_card_in_7()[1]): print('Draw!')
            if value(self.hand_ranking()) == 8:                                                                                    # If ranks draw in One pair
                if value(self.high_card_in_8()) > value(other.high_card_in_8()): print(f'Player {self.players} Win!')
                if value(self.high_card_in_8()) < value(other.high_card_in_8()): print(f'Player {other.players} Win!')
                if value(self.high_card_in_8()) == value(other.high_card_in_8()): print('Draw!')

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
    
    # your test cases here
    a_player_deck = Hands(['2C','5H','QD','QS','TH'],'A')
    b_player_deck = Hands(['3D','4C','4S','3H','3C'],'B')
    a_player_deck.match(b_player_deck)

    a_player_deck = Hands(['2C','2H','QD','QS','QH'],'A')
    b_player_deck = Hands(['3D','3C','KS','KH','KC'],'B')
    a_player_deck.match(b_player_deck)
