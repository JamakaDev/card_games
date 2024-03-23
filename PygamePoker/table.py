import pygame
from time import sleep
from card import Card
from deck import Deck
from menu import Menu
from settings import *


class Table():
  def __init__(self):
    self.display_surface = pygame.display.get_surface()
    self.cut_card = Card((POSITIONS['DECK']), 'Cut_Card.png')
    self.burn_card = Card((POSITIONS['BURN']), 'Burn_Card.png')
    self.deck = Deck()
    self.menu = Menu()
    self.player = []
    self.dealer = []
    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.all_sprites.add(self.deck.deck_of_cards)
    self.all_sprites.add(self.deck.used_cards)
    self.all_sprites.add(self.cut_card)
    self.all_sprites.add(self.burn_card)

    

  def shuffle_cards(self,times=1):
    self.deck.shuffle_deck(times)
    for card in self.deck.deck_of_cards: card.rect.update(POSITIONS['DECK'], CARD_SIZE)
    self.all_sprites.move_to_front(self.cut_card)
    self.all_sprites.move_to_front(self.burn_card)

    

  def deal_card(self, key):
    card = self.deck.get_card()
    card.rect.update(POSITIONS[key],(CARD_SIZE))    
    self.all_sprites.move_to_front(card) if card else None


  def deal_hole_cards(self, idx):
    for i in range(2):
      card1 = self.deck.get_card()
      card2 = self.deck.get_card()

      card1.rect.update(POSITIONS['PLAYER'][idx],(CARD_SIZE))
      card2.rect.update(POSITIONS['DEALER'][idx],(CARD_SIZE))
      
      self.player.append(card1)
      self.dealer.append(card2)
          
      self.deck.used_cards.append(card1)
      self.deck.used_cards.append(card2)

      if idx == 1: 
        self.all_sprites.move_to_front(card1)
        self.all_sprites.move_to_front(card2)


  def deal_flop_cards(self):
    burn_card = self.deck.get_card()
    burn_card.rect.update(POSITIONS['BURN'],(CARD_SIZE))
    self.deck.used_cards.append(burn_card)
    for i in range(3):
      card = self.deck.get_card()
      card.rect.update(POSITIONS['FLOP'][i],(CARD_SIZE))
      self.deck.used_cards.append(card)
      

  def deal_turn_card(self):
      burn_card = self.deck.get_card()
      burn_card.rect.update(POSITIONS['BURN'],(CARD_SIZE))
      
      card = self.deck.get_card()
      card.rect.update(POSITIONS['TURN'],(CARD_SIZE))

      self.deck.used_cards.append(burn_card)
      self.deck.used_cards.append(card)
  
  
  def deal_river_card(self):
      burn_card = self.deck.get_card()
      burn_card.rect.update(POSITIONS['BURN'],(CARD_SIZE))
      
      card = self.deck.get_card()
      card.rect.update(POSITIONS['RIVER'],(CARD_SIZE))

      self.deck.used_cards.append(burn_card)
      self.deck.used_cards.append(card)

          
  def fold_hand(self):
    # while self.player:
      # card = self.player.pop()
      # card.rect.update(POSITIONS['MUCK'],(CARD_SIZE))
    self.player.clear()
    self.dealer.clear()
    self.shuffle_cards(times=1)
    

  def check_menu(self, curson_position):
    if self.menu.shuffle_rect.collidepoint(curson_position):
      self.shuffle_cards()
      sleep(.25)
      
    if self.menu.deal_rect.collidepoint(curson_position):
      if len(self.player) > 2: return
      self.deal_hole_cards(1) if len(self.player) else self.deal_hole_cards(0)
      sleep(.25)

    if self.menu.fold_rect.collidepoint(curson_position):
      self.fold_hand()
      sleep(.25)

    if self.menu.flop_rect.collidepoint(curson_position):
      self.deal_flop_cards()
      sleep(.25)

    if self.menu.turn_rect.collidepoint(curson_position):
      self.deal_turn_card()
      sleep(.25)
      
    if self.menu.river_rect.collidepoint(curson_position):
      self.deal_river_card()
      sleep(.25)
  
  def start(self):
    self.menu.draw()
    self.all_sprites.draw(self.display_surface)
    for card in self.deck.used_cards + [self.cut_card] + [self.burn_card]: card.draw()

    self.all_sprites.update()
    
