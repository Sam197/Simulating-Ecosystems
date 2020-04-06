import pygame
import random
import os

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PICTURE_SIZE = 20
TILE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'tree.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'land.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'water.png'))) ]

class Rabbit:
    def __init__(self, x, y):
        pass

class Tile:
    def __init__(self, x, y, surface, growable):
        self.x = x
        self.y = y
        self.surface_image = surface
        self.isgrowable = growable

    def display(self, screen):
        screen.blit(self.surface_image, (self.x, self.y))

def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    xcoord = 0
    ycoord = 0

    for ycoord in range(0, SCREEN_HEIGHT, PICTURE_SIZE):

        for xcoord in range(0, SCREEN_WIDTH, PICTURE_SIZE):

            image_tile = TILE_IMGS[random.randint(0,2)]

            screen.blit(image_tile, (xcoord, ycoord))

    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

main()