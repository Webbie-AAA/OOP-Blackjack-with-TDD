class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank.upper()
        self.suit = suit.upper()

    def to_string(self) -> str:
        """Returns the correct string to represent the card"""
        return f"{self.rank}{self.suit}"
        ...

    def get_points(self) -> int:
        """Gets the correct number of points for a card"""

        ranks_dict = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                      "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
        points = ranks_dict[self.rank]
        return points
        ...


class Hand:
    def __init__(self, cards: list) -> None:
        all_cards = all(isinstance(card, Card) for card in cards)

        if (not all_cards):
            raise Exception('A Hand can only contain Cards')

        self.cards = cards

    def get_points(self) -> int:
        """Calculates the total points for a hand of cards"""
        points = 0
        for card in self.cards:
            points += card.get_points()

        if points == 22:
            for card in self.cards:
                if "A" in card.to_string():
                    points -= 1
                    break
        return points
        ...


class Deck:
    def __init__(self) -> None:
        # TODO Complete this method so the deck contains all the correct cards
        self.cards: list[Card] = []
        ranks = ["A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["S", "D", "C", "H"]
        for suit in suits:
            for rank in ranks:
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def draw(self) -> Card:
        """Removes and returns the top card from the deck"""
        return self.cards.pop(0)

    def get_cards(self) -> list[Card]:
        ...

    def shuffle(self) -> None:
        """Shuffles the cards in this deck"""
        print(self.cards)
