import pygame, sys
from settings import *
from level import Level
class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH)) # window
        pygame.display.set_caption("Zelda") # title
        self.clock = pygame.time.Clock()

        self.level = Level() # 2. initialize level

    def run(self):
        while True:

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game() # 1. main game class
    game.run()