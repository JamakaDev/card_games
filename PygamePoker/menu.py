import pygame
from settings import *

pygame.font.init()

class Menu():
  def __init__(self):
    self.display_surface = pygame.display.get_surface()
    
    self.font = pygame.font.SysFont("orange juice", 48, True)
    
    self.shuffle = self.font.render('Shuffle', True, 'black')
    self.shuffle_rect = self.shuffle.get_rect(topleft=POSITIONS['SHUFFLE'])
    
    self.deal = self.font.render('Deal', True, 'black')
    self.deal_rect = self.deal.get_rect(topleft=POSITIONS['DEAL'])
    
    self.fold = self.font.render('Fold', True, 'red')
    self.fold_rect = self.fold.get_rect(topleft=POSITIONS['FOLD'])

    self.flop = self.font.render('Flop', True, 'black')
    self.flop_rect = self.flop.get_rect(topleft=POSITIONS['DEAL_FLOP'])

    self.turn = self.font.render('Turn', True, 'black')
    self.turn_rect = self.turn.get_rect(topleft=POSITIONS['DEAL_TURN'])

    self.river = self.font.render('River', True, 'black')
    self.river_rect = self.river.get_rect(topleft=POSITIONS['DEAL_RIVER'])

    


  def draw(self):
    self.display_surface.blit(self.shuffle, self.shuffle_rect)
    self.display_surface.blit(self.deal, self.deal_rect)
    self.display_surface.blit(self.fold, self.fold_rect)
    self.display_surface.blit(self.flop, self.flop_rect)
    self.display_surface.blit(self.turn, self.turn_rect)
    self.display_surface.blit(self.river, self.river_rect)

    