from random import random

from model.Card import Card
from model.Rank import Rank
from model.Suit import Suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))



