# This is a sample Python script.
import random
import sys

from model.Deck import Deck
from model.Player import Player


def start_game(number_of_players):
    if number_of_players < 2 or number_of_players > 4:
        sys.exit("Invalid number of players: " + str(
            number_of_players) + ". Minimum number of players is 2 and maximum is 4")
    deck = Deck()
    random.shuffle(deck.cards)
    print("Initialized deck with " + str(len(deck.cards)) + " cards: ", deck.cards)
    players = register_players(number_of_players)
    dispense_cards(players, deck)


def register_players(number_of_players):
    players = []
    for player_number in range(number_of_players):
        name = input("Register player " + str(player_number) + ":")
        player = Player(name, [], [], [])
        players.append(player)
    print("Registered " + str(number_of_players) + " players: ", players)
    return players


def dispense_cards(players, deck):
    for player in players:
        for card in range(3):
            player.hidden_cards.append(deck.cards.pop())
            player.open_cards.append(deck.cards.pop())
            player.hand.append(deck.cards.pop())
        print("Open cards of player " + player.name + ": ", player.open_cards)
    print("Remaining deck: ", len(deck.cards))


if __name__ == '__main__':
    start_game(2)
