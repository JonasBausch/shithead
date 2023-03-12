class Player:
    def __init__(self, name, hidden_cards, open_cards, hand):
        self.name = name
        self.hidden_cards = hidden_cards
        self.open_cards = open_cards
        self.hand = hand

    def __repr__(self):
        return self.name
