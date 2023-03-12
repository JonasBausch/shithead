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
    pile = deck.cards
    graveyard = []
    for player in players:
        trade_cards(player)
    # TODO now the actual game starts.


def trade_cards(player):
    exchange_card = input(player.name + ", do you want to exchange a card? ")
    while exchange_card == "yes":
        print("Which card do you want to exchange? Available cards on hand: ", player.hand_cards)
        card_on_hand = None
        while not card_on_hand:
            card_on_hand = card_from_input(player.hand_cards)
        print("Which card do you want to trade it for? Available open cards: ", player.open_cards)
        card_to_exchange = None
        while not card_to_exchange:
            card_to_exchange = card_from_input(player.open_cards)
        exchange_cards(player, card_on_hand, card_to_exchange)
        exchange_card = input("Do you want to exchange another card? ")
    print("Done exchanging cards for player " + player.name)


def exchange_cards(player, card_on_hand, card_to_exchange):
    player.hand_cards.pop(player.hand_cards.index(card_on_hand))
    player.hand_cards.append(card_to_exchange)
    player.open_cards.pop(player.open_cards.index(card_to_exchange))
    player.open_cards.append(card_on_hand)
    print("Hand cards after exchange: ", player.hand_cards)
    print("Open cards after exchange: ", player.open_cards)


def card_from_input(cards):
    rank = input("Rank: ")
    suit = input("Suit: ")
    selected_card = None
    try:
        selected_card = next(
            (card for card in cards if card.rank == Rank[rank] and card.suit == Suit[suit]), None)
    except:
        print(rank + " of " + suit + " cannot be resolved to a valid card")
        return
    if not selected_card:
        print("Couldn't find card " + rank + " of " + suit + " in ", cards)
        return
    elif selected_card:
        print("Selected card: ", selected_card)
        return selected_card


def initialize_deck():
    deck = Deck()
    random.shuffle(deck.cards)
    print("Initialized deck with " + str(len(deck.cards)) + " cards: ", deck.cards)
    return deck


def register_players(number_of_players):
    players = []
    for player_number in range(number_of_players):
        name = input("Register player " + str(player_number) + ": ")
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
