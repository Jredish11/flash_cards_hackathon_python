import pdb
from card import Card
from turn import Turn
from deck import Deck

def test_deck_exists():
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    assert isinstance(deck, Deck)

def test_deck_has_cards():
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    assert deck.cards == cards