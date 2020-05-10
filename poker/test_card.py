import pytest
from card import suits, ranks, Card, PKCard, Deck

def test_PKCard_init():
    card = PKCard('AC')
    assert card.rank == 'A' and card.suit == 'C'

def test_PKCard_init_exception():
    for face in ['10S', 'BD', 'TA']:
        with pytest.raises(ValueError):
            PKCard(face)

def test_PKCard_repr():
    assert repr(PKCard('AC')) == 'AC'

@pytest.fixture
def all_faces():
    return [r+s for r in ranks for s in suits]

def test_PKCard_value(all_faces):
    for face in all_faces:
        card, excepted = PKCard(face), PKCard.VALUES[face[0]]
        assert card.value() == excepted

@pytest.fixture
def c9C():
    return PKCard('9C')

@pytest.fixture
def c9H():
    return PKCard('9H')

@pytest.fixture
def cTH():
    return PKCard('TH')

def test_PKCard_comp(c9C, c9H, cTH):
    assert c9C == c9C and c9C == c9H
    assert c9H < cTH and c9C < cTH
    assert c9C <= c9H <= cTH
    assert cTH >= c9H and cTH > c9C
    assert cTH >= c9H >= c9C
    assert c9C != cTH and c9H != cTH

def test_PKCard_sort(all_faces):
    all_cards = [PKCard(r+s) for r in ranks for s in suits]
    import random
    random.shuffle(all_cards)
    all_cards.sort()

@pytest.fixture
def deck():
    return Deck(PKCard)

def test_Deck_init(deck):
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], PKCard)

def test_Deck_pop(deck):
    card = deck.pop()
    assert card.rank == ranks[-1] and card.suit == suits[-1] \
        and len(deck.cards) == 52-1

def test_Deck_len(deck):
    deck.pop(); deck.pop()
    assert len(deck.cards) == deck.__len__() == len(deck)

def test_Deck_getitem(deck):
    assert (deck[10].rank, deck[10].suit) \
        == (deck.cards[10].rank, deck.cards[10].suit)

