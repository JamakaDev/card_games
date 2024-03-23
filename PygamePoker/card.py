import pygame
from settings import *

class Card(pygame.sprite.Sprite):
    def __init__(self, position, image_file):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load(f'./images/{image_file}').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (CARD_WIDTH*1.5, CARD_HEIGHT*1.5))
        self.rect = self.image.get_rect(topleft=position)  
        self._layer = self.rect.bottom


    def draw(self):
        pygame.draw.rect(self.display_surface, (0,0,0), [self.rect.x, self.rect.y, CARD_WIDTH*1.5, CARD_HEIGHT*1.5], 3, 10)
        
        
