import pygame, sys

PIXEL = 22.64

## drawing

CAPTION = "CISS450: self driving car"
FRAME_RATE = 30.0
MILLISEC_PER_FRAME = 1000.0 / FRAME_RATE
# SIZE = (44, 35)
SIZE = (1000, 800)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRASS_COLOR = (56, 102, 0)

## viewwindow

WORLD_W = 44
WORLD_H = 35.3
VIEW_X = 0
VIEW_Y = 0
VIEW_W = 1000
VIEW_H = 800

## roads

ROAD_X = 161.83
ROAD_Y = 20
NUM_LANES = 6
LANE_WIDTH = 3.66
ROAD_HEIGHT = WORLD_H
ROAD_END = ROAD_X + (LANE_WIDTH * NUM_LANES)
## dividers

divider_width = 0.65
# DIVIDER_WIDTH = LANE_WIDTH/15
DIVIDER_WIDTH = 0.65
DIVIDER_HEIGHT = 2
DIVIDER_SPACING = 1
DIVIDER_COLOR = (240, 240, 240)
ROAD_COLOR = (20, 20, 20)


## images

car_image = pygame.image.load("images/small/Black_viper/Black_viper.png")
audi_image = pygame.image.load("images/small/Audi/Audi.png")
mini_truck_image = pygame.image.load("images/small/Mini_truck/Mini_truck.png")
ambulance_image = pygame.image.load("images/small/Ambulance/Ambulance.png")
police_image = pygame.image.load("images/small/Police/Police.png")
taxi_image = pygame.image.load("images/small/taxi/taxi.png")
mini_van_image = pygame.image.load("images/small/Mini_van/Mini_van.png")
black_viper_image = pygame.image.load("images/small/Black_viper/Black_viper.png")

# Sensor Info
MAX_RADIUS = 4
