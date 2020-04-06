import pygame
import random
import os

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PICTURE_SIZE = 20
TILE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'tree.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'land.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'water.png'))) ]
RABBIT_IMG = pygame.image.load(os.path.join('images', 'rabbit.png'))

class Rabbit:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.rabbit_img = img

    def display(self, screen):
        screen.blit(self.rabbit_img, (self.x, self.y))

class Tile:
    def __init__(self, x, y, surface, solid, growable):
        self.x = x
        self.y = y
        self.surface_image = surface
        self.isSolid = solid
        self.isgrowable = growable
    
    def checkIsSolid(self):
        if self.isSolid:
            return True
        else:
            return False

    def checkIsGrowable(self):
        if self.isgrowable:
            return True
        else:
            return False
    
    def returnXandY(self):
        return (self.x, self.y)

    def changeImg(self, img):
        self.surface_image = img

    def display(self, screen):
        screen.blit(self.surface_image, (self.x, self.y))

def create_grid():
    backend_grid = []
    xcoord = 0
    ycoord = 0

    for ycoord in range(0, SCREEN_HEIGHT, PICTURE_SIZE):
        placeholder = []
        for xcoord in range(0, SCREEN_WIDTH, PICTURE_SIZE):
            placeholder.append(Tile(xcoord, ycoord, TILE_IMGS[random.randint(0,2)], False, False))
        backend_grid.append(placeholder)
        del placeholder

    return backend_grid

def displayAll(backend_grid, rabbit, screen):
    for row in backend_grid:
        for col in row:
            col.display(screen)
            #print(col.returnXandY())
    rabbit.display(screen)

def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    backend_grid = create_grid()
    #print(vars(backend_grid[0][0])['isSolid']) # finds value of property of a cirtain tile object
    rabbit = Rabbit(vars(backend_grid[random.randint(0,29)][random.randint(0,49)])['x'], vars(backend_grid[random.randint(0,29)][random.randint(0,49)])['y'], RABBIT_IMG)

    running = True

    while running:
        
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rabbit = Rabbit(vars(backend_grid[random.randint(0,29)][random.randint(0,49)])['x'], vars(backend_grid[random.randint(0,29)][random.randint(0,49)])['y'], RABBIT_IMG)

        #backend_grid[random.randint(0,29)][random.randint(0,49)].changeImg(TILE_IMGS[2])
        displayAll(backend_grid, rabbit, screen)

        #running = False
        pygame.display.update()

main()
