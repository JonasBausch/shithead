# This is a sample Python script.
import random

from model.Deck import Deck
from model.Player import Player


def start_game(number_of_players):
    deck = Deck()
    random.shuffle(deck.cards)
    print("Initialized deck with " + str(len(deck.cards)) + " cards: ", deck.cards)
    players = []
    for player_number in range(number_of_players):
        name = input("Register player " + str(player_number) + ":")
        player = Player(name, [], [], [])
        players.append(player)
    print("Registered " + str(number_of_players) + " players: ", players)


if __name__ == '__main__':
    start_game(4)

