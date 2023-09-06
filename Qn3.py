"""
Write a program to:
a) Shuffle a deck of cards
b) To choose one single card from the deck
c) To create a random sample of size 2 from available deck of cards
"""

import random


def shuffleCards():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5",
             "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = [(ranks, suit) for ranks in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def chooseCard(deck):
    return random.choice(deck)


def createSample(deck, sample_size):
    return random.sample(deck, sample_size)


def main():
    deck = shuffleCards()
    sample_size = 2
    print(deck)
    print("\nThe deck is:", chooseCard(deck))
    print("\nThe sample is:", createSample(deck, sample_size))


main()
