# This is a sample Python script.
import random
import sys

from model.Deck import Deck
from model.Player import Player
from model.Rank import Rank
from model.Suit import Suit


def start_game(number_of_players):
    if number_of_players < 2 or number_of_players > 4:
        sys.exit("Invalid number of players: " + str(
            number_of_players) + ". Minimum number of players is 2 and maximum is 4")
    deck = initialize_deck()
    players = register_players(number_of_players)
    dispense_cards(players, deck)
    for player in players:
        exchange_cards(player)


def exchange_cards(player):
    exchange = input("Do you want to exchange a card? ")
    while exchange == "yes":
        print("Which card do you want to exchange? Available cards on hand: ", player.hand_cards)
        rank = input("Rank: ")
        suit = input("Suit: ")
        card_on_hand = next(
            (card for card in player.hand_cards if card.rank == Rank[rank] and card.suit == Suit[suit]), None)
        print("Selected card on hand: ", card_on_hand)
        print("Which card do you want to trade it for? Available open cards: ", player.open_cards)
        rank = input("Rank: ")
        suit = input("Suit: ")
        card_to_exchange = next(
            (card for card in player.open_cards if card.rank == Rank[rank] and card.suit == Suit[suit]), None)
        # TODO pop doesn't work with objects, only indices. find a way to remove card_on_hand from hand_cards
        player.hand_cards.pop(card_on_hand)
        player.hand_cards.append(card_to_exchange)
        player.open_cards.pop(card_to_exchange)
        player.open_cards.append(card_on_hand)
        print("open cards after exchange: ", player.open_cards)
        print("hand cards after exchange: ", player.hand_cards)
        exchange = input("Do you want to exchange another card? ")
    print("Done exchanging cards for player " + player.name)


def initialize_deck():
    deck = Deck()
    random.shuffle(deck.cards)
    print("Initialized deck with " + str(len(deck.cards)) + " cards: ", deck.cards)
    return deck


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
            player.hand_cards.append(deck.cards.pop())
        print("Open cards of player " + player.name + ": ", player.open_cards)
    print("Remaining deck: ", len(deck.cards))


if __name__ == '__main__':
    start_game(2)
