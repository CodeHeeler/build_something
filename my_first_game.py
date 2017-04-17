import pygame, sys, random
from pygame.locals import *

TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 20

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)

# change to "textures" and add png files of same pixel size
colours = {
            DIRT: BROWN,
            GRASS: GREEN,
            WATER: BLUE,
            COAL: BLACK,
            ROCK: GREY,
            LAVA: RED
}

tilemap = [[DIRT for w in range (MAPWIDTH)] for h in range (MAPHEIGHT)]

# tilemap = [
#             [GRASS, COAL, DIRT, ROCK, LAVA],
#             [WATER, WATER, GRASS, ROCK, LAVA],
#             [ROCK, LAVA, COAL, GRASS, WATER],
#             [LAVA, ROCK, DIRT, GRASS, COAL],
#             [GRASS, WATER, DIRT, ROCK, LAVA]
# ]

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
pygame.display.set_caption('My First 2D-MineCraft Game')

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,15)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1:
            tile = ROCK
        elif randomNumber == 2 or randomNumber == 3:
            tile = WATER
        elif randomNumber >= 4 and randomNumber <= 10:
            tile = GRASS
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
    pygame.display.update()
