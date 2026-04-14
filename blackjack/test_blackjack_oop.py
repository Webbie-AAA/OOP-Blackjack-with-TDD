# pylint: skip-file

from blackjack_oop import Deck, Card, Hand
import pytest


@pytest.fixture
def jack_of_hearts():
    return Card('J', 'H')


@pytest.fixture
def three_of_spades():
    return Card('3', 'S')


@pytest.fixture
def ace_of_diamonds():
    return Card('A', 'D')


@pytest.fixture
def ace_of_clubs():
    return Card('A', 'C')


def test_card_rank(jack_of_hearts):
    assert jack_of_hearts.rank == 'J'


def test_card_suit(jack_of_hearts):
    assert jack_of_hearts.suit == 'H'


def test_card_uppercased():
    card = Card('J', 'h')
    assert card.suit == 'H'


def test_card_points(jack_of_hearts, three_of_spades):
    assert jack_of_hearts.get_points() == 10
    assert three_of_spades.get_points() == 3


def test_card_to_string(jack_of_hearts, three_of_spades):
    assert jack_of_hearts.to_string() == "JH"
    assert three_of_spades.to_string() == "3S"


def test_hand_raise_exception():
    with pytest.raises(Exception):
        Hand(['AC', '7H'])


def test_hand_points_empty():
    assert Hand([]).get_points() == 0


def test_hand_points_numbers_only():
    hand = Hand([Card('7', 'H'),  Card('2', 'D')])
    assert hand.get_points() == 9


def test_hand_points_numbers_and_face():
    hand = Hand([
        Card('3', 'D'),
        Card('J', 'C'),
        Card('Q', 'H'),
        Card('2', 'H'),
        Card('A', 'C')
    ])
    assert hand.get_points() == 36


def test_hand_points_two_aces(ace_of_diamonds, ace_of_clubs):
    hand = Hand([ace_of_diamonds,  ace_of_clubs])
    assert hand.get_points() == 21


def test_hand_points_two_aces_and_others(ace_of_diamonds, ace_of_clubs):
    hand = Hand([
        Card('2', 'D'),
        ace_of_diamonds,  ace_of_clubs
    ])
    assert hand.get_points() == 24


def test_deck_generate_order():
    deck = Deck()

    cards_in_deck = [deck.draw().to_string() for i in range(len(deck.cards))]

    assert cards_in_deck == [
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"
    ]
