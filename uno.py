# A deck of cards
# A hand of cards for each player
# A discard pile
# A draw pile
# Two kinds of players: human and computer
# The flow of turns between players
# The end of the game

# 108 Cards
# Red, Blue, Green, Yellow
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, Reverse, Draw 2, Skip
# Draw 4, Change colour


# Build the deck
# Give each player 7 cards
# Start with one card in discard
# if wild card, player or computer can choose colour

import random


def build_deck():

    deck = []
    colours = ["Red", "Blue", "Green", "Yellow"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Reverse", "Draw 2", "Skip"]
    wild_cards = ["Wild", "Wild Draw 4"]

    for colour in colours:
        for value in values:
            cards_combined = "{} {}".format(value, colour)
            deck.append(cards_combined) 

    for wild_card in wild_cards:
        deck.append(wild_card)

    return deck
            
            
def discard_pile():
    pass

def draw_pile():
    pass

def players():
    pass

def turns():
    pass

def end_game():
    pass


print(build_deck())

