import pygame
from sys import exit
from settings import *
from table import Table



# from debug import debug


class Game:
    def __init__(self):          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Kardz')
        self.clock = pygame.time.Clock()
        self.running = False
        self.table = Table()


    def draw_screen(self):
        
        self.screen.fill('white')
        self.table.start()
               
        pygame.display.update()
        self.clock.tick(FPS)


    def run(self):
      self.running = True
      while self.running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.running = False
              pygame.quit()
              exit('You closed the program!')
          
            
        mouse_position = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        if mouse_clicked[0]:
          self.table.check_menu(mouse_position)
          
        self.draw_screen()

           


            
            
            

if __name__ == '__main__':
    game = Game()
    game.run()

