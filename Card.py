class Card:
    """Одна игральная карта"""

    RANKS = ["T","2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "Д", "K"]
    
    #♠ ♣ ♥ ♦
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit 
        return rep 


class Hand:
    """Рука: набор карт на руках у одного игрока."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + "\t"

        else:
            rep = "<пусто>"
        return rep