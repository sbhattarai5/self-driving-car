"""

"""

import pygame, sys
pygame.init()
pygame.display.set_caption("CISS450: self driving car")

SIZE = (1000, 800)

RED = (255, 0, 0)
WHITE = (255, 255, 255)

DIVIDER_COLOR = (240, 240, 240)
GRASS_COLOR = (56, 102, 0)
ROAD_COLOR = (20, 20, 20)

ROAD_X = 0
ROAD_Y = 0
NUM_LANES = 2
LANE_WIDTH = 120
ROAD_HEIGHT = 800

DIVIDER_WIDTH = LANE_WIDTH/15
DIVIDER_HEIGHT = 40
DIVIDER_SPACING = 40

FONT48 = pygame.font.SysFont(None, 48)

road_rect = pygame.Rect(160, 0, NUM_LANES * LANE_WIDTH,  SIZE[1])
