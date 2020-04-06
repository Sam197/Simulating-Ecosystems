import pygame
import random
import os
import time

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PICTURE_SIZE = 20
TILE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'tree.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'land.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'water.png'))) ]
RABBIT_IMG = pygame.image.load(os.path.join('images', 'rabbit.png'))
start = time.time()

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
        self.grow_frame = random.randint(2000, 4000)
        self.frame_to_grow = self.grow_frame
        self.has_changed = True
    
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
        self.has_changed = True
    
    def tile_frame(self, frame):
        if self.surface_image != TILE_IMGS[2]:
            if frame == self.frame_to_grow:
                self.surface_image = TILE_IMGS[0]
                self.frame_to_grow += self.grow_frame
                print("TREE")
                self.has_changed = True

    def display(self, screen):
        screen.blit(self.surface_image, (self.x, self.y))
        self.has_changed = False

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
#hello1
def place_rabbit(backend_grid, previous_rabbit_pos, screen):
    backend_grid[previous_rabbit_pos[0]][previous_rabbit_pos[1]].display(screen)
    previous_rabbit_pos.clear()
    while True:
        y = random.randint(0,29)
        x = random.randint(0,49)
        if backend_grid[y][x].surface_image != TILE_IMGS[2]:
            rabbit = Rabbit(vars(backend_grid[y][x])['x'], vars(backend_grid[y][x])['y'], RABBIT_IMG)
            break
    if vars(backend_grid[y][x])['surface_image'] == TILE_IMGS[0]:
        backend_grid[y][x].changeImg(TILE_IMGS[1])
    previous_rabbit_pos.append(y)
    previous_rabbit_pos.append(x)
    print(previous_rabbit_pos)
    return rabbit

def displayAll(backend_grid, rabbit, screen, frame, previous_rabbit_pos):
    for row in backend_grid:
        for col in row:
            col.tile_frame(frame)
            if vars(col)['has_changed']:
                col.display(screen)
            #print(col.returnXandY())
    pygame.display.update()
    rabbit.display(screen)

def main():
    
    running = True
    frame = 0
    rabbit_frame = 100
    previous_rabbit_pos = [0,0]

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    backend_grid = create_grid()
    #print(vars(backend_grid[0][0])['isSolid']) # finds value of property of a cirtain tile object
    rabbit = place_rabbit(backend_grid, previous_rabbit_pos, screen)
    displayAll(backend_grid, rabbit, screen, frame, previous_rabbit_pos)

    while running:
        
        #screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rabbit = place_rabbit(backend_grid, previous_rabbit_pos, screen)

        if frame == rabbit_frame:
            rabbit = place_rabbit(backend_grid, previous_rabbit_pos, screen)
            rabbit_frame += 100

        #backend_grid[random.randint(0,29)][random.randint(0,49)].changeImg(TILE_IMGS[2])
        displayAll(backend_grid, rabbit, screen, frame, previous_rabbit_pos)

        #running = False
        pygame.display.update()
        frame += 1
        print(frame)

main()
print(time.time()-start)