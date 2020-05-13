# coding: utf-8

# ***Jupyter Notebook에서 Download as Python으로 받으세요.***
# # PA. Find poker hands
# 포커 게임은 손에 든 패 5장을(hands라 한다) 가지고 hand의 ranking category(포커 족보)가 높은 쪽이 이기는 게임이다.
# 
# 족보에 있는지 알아 보려면, 기본적으로 다음을 check 해야 한다.
# - 5장 모두 suit이 같은지 (`is_flush`)
# - 5장 모두 rank가 연속되었는지 (`is_straight`)
# - 같은 rank가 2장인지, 3장인지, 4장인지에 따른 hand_ranking 명 (`find_a_kind`)
# 
# `tell_hand_ranking` 함수는 위 function을 이용하여 종합 판정한 결과로
# hand ranking name을 return해야 한다.
# 
# 아래 주어진 function들을 구현하고,
# 이들이 잘 동작함을 보여주는 test case들을 만들어 시험하고 그 결과도 제출하라.
# 
# 제출요령: VS code IDE를 이용하여 script 파일을 만들고 source와 test가 실행된 결과 화면을 zip으로 압축하여 제출한다.
# 
# 참고: [List of poker hands](http://en.wikipedia.org/wiki/List_of_poker_hands)
# - Joker는 없는 것으로 한다. 따라서 'Five of a kind'는 족보에 없다.

# 편의상 suit과 rank는 문자 하나로 표기한다. 따라서 card는 a rank와 a suit으로 구성되므로 2개의 문자나 deckle로 표현할 수 있다. 
# 그리고 sorting 편의를 위해 rank를 suit 전에 두기로 한다.
# 
# 예: '3C' 또는 ('3', 'C')

import copy
import sys

suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))

def is_flush(cards):
    if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1] : return True
    else: return False
    
def is_straight(cards):
    sorted(cards)
    if int(cards[0][0])+2 == int(cards[1][0])+1 == int(cards[2][0]) == int(cards[3][0])-1 == int(cards[4][0])-2: return True
    else: return False
    
def classify_by_rank(cards):
    classified = copy.deepcopy(values)
    for i in classified: classified[i] = 0
    for i in range(len(deck_original)): classified[deck_original[i][0]] += 1
    return classified
    
def find_a_kind(cards):
    cards_by_ranks = classify_by_rank(cards)
    pair = 0
    triple = 0
    fourcard = 0
    ranking = 0
    for i in cards_by_ranks:
        if cards_by_ranks[i] == 2: pair += 1
        if cards_by_ranks[i] == 3: triple += 1
        if cards_by_ranks[i] == 4: fourcard += 1
    if is_straight(cards) == True and is_flush(cards) == True : ranking = 1
    elif fourcard == 1: ranking = 2
    elif pair == 1 and triple ==1: ranking = 3
    elif is_flush(cards) == True : ranking = 4
    elif is_straight(cards) == True : ranking = 5
    elif triple == 1: ranking = 6
    elif pair == 2: ranking = 7
    elif pair == 1: ranking = 8
    else : ranking = 9
    return ranking

def tell_hand_ranking(cards):
    if find_a_kind(cards) == 1: return 'Straight Flush (rank 1)'
    elif find_a_kind(cards) == 2: return 'Four of a kind (rank 2)'
    elif find_a_kind(cards) == 3: return 'Full house (rank 3)'
    elif find_a_kind(cards) == 4: return 'Flush (rank 4)'
    elif find_a_kind(cards) == 5: return 'Straight (rank 5)'
    elif find_a_kind(cards) == 6: return 'Three of a kind (rank 6)'
    elif find_a_kind(cards) == 7: return 'Two pair (rank 7)'
    elif find_a_kind(cards) == 8: return 'One pair (rank 8)'
    elif find_a_kind(cards) == 9: return 'High card (rank 9)'

def input_your_cards():

        deck = input("Write information of your five cards one by one with comma separately. (10 is T, 11 is J, 12 is Q, 13 is K and 14 is A) : ").upper().split(',')
        deck_original.append(deck)
        temp = deck[0]
        if deck[0] == 'T': temp = '10'
        elif deck[0] == 'J': temp = '11'
        elif deck[0] == 'Q': temp = '12'
        elif deck[0] == 'K': temp = '13'
        elif deck[0] == 'A': temp = '14'

        if deck in your_cards:
            print("Trump card has only one unique number and one pattern of cards. Please try again.")
            sys.exit()
        if deck[1] not in suits:
            print("The pattern of the cards must be one of S,D,H,C. Plase try again.")
            sys.exit()
        if int(temp) < 2 or int(temp) > 14:
            print("The number of the cards must be over 2 under 14. Please try again.")
            sys.exit()
        your_cards.append(deck)

if __name__ == "__main__":
    your_cards = list()
    deck = list()
    global deck_original
    deck_original = list()
    suits = list(suits)
    for i in range(5):
        input_your_cards()
        print('Current my deck is : ', end = '')
        print(your_cards)
    
    print(tell_hand_ranking(your_cards))