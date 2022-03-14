import pygame
from settings import *
from tile import Tile
from player import Player


class Level:

    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE # x position of the tile
                y = row_index * TILESIZE # y position of the tile
                if col == "X":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites]) # initialize rock at the pos
                elif col == "P":
                    Player((x, y), [self.visible_sprites]) # initialize player at position



    def run(self):
        self.visible_sprites.draw(self.display_surface)

