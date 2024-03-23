import random
import time
from cards import *


def create_deck():
    return CLUBS + DIAMONDS + HEARTS + SPADES

def shuffle_deck(deck, num_of_shuffles=1):
    for each_shuffle in range(num_of_shuffles):
        print('Shuffling the deck...')
        time.sleep(2)
        random.shuffle(deck)
    return deck

def cut_deck(deck, num_of_cuts=1):
    for each_cut in range(num_of_cuts):
        print('Cutting the deck...')
        time.sleep(2)
        idx = random.randint(0, 26)
        deck = deck[idx:] + deck[:idx]
    return deck

def deal_card(deck):
    card = deck.pop(0)
    print(f'Here\'s the {card}')
    return card

def display_deck(deck):
    for card in deck:
        print(card)
