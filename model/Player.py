class Player:
    def __init__(self, name, hidden_cards, open_cards, hand_cards):
        self.name = name
        self.hidden_cards = hidden_cards
        self.open_cards = open_cards
        self.hand_cards = hand_cards

    def __repr__(self):
        return self.name
