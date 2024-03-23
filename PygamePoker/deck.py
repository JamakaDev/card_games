import pygame
from random import shuffle
from os import listdir, system
from time import sleep
from settings import *


from card import Card

class Deck():
    def __init__(self):
      self.display_surface = pygame.display.get_surface()
      self.deck_of_cards = self.create_deck()
      self.used_cards = list()
      # self._layer = self.rect.bottom

    
    def create_deck(self):
        return list(Card((POSITIONS['DECK']), card) for card in listdir('images') if 'Card' not in card)

    
    def shuffle_deck(self, number_of_shuffles=3):
        if self.deck_of_cards != 52: 
            self.deck_of_cards += self.used_cards
            self.used_cards.clear()
        
        for idx in range(number_of_shuffles): 
            if not idx: system('cls')
            for i in range(1, 5):
                print(f'Shuffling the deck{"." * i}')
                sleep(1)
                system('cls')                
            shuffle(self.deck_of_cards)
            
         
            
    

    def get_card(self):
      if self.deck_of_cards:
        card = self.deck_of_cards.pop()
        self.used_cards.append(card)
        return card
      return
        
