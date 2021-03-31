"""
   The configuration of the simulation
"""

import pygame, sys

## drawing

CAPTION = "CISS450: self driving car"
FRAME_RATE = 30.0
MILLISEC_PER_FRAME = 1000.0/FRAME_RATE
SIZE = (1000, 800)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DIVIDER_COLOR = (240, 240, 240)
GRASS_COLOR = (56, 102, 0)
ROAD_COLOR = (20, 20, 20)

## computation

ROAD_X = 0
ROAD_Y = 0
NUM_LANES = 2
LANE_WIDTH = 120
ROAD_HEIGHT = 800


divider_width = 10
DIVIDER_WIDTH = LANE_WIDTH/15
DIVIDER_HEIGHT = 40
DIVIDER_SPACING = 40

## images

car_image = pygame.image.load('images/small/Black_viper/Black_viper.png')
audi_image = pygame.image.load('images/small/Audi/Audi.png')
mini_truck_image = pygame.image.load('images/small/Mini_truck/Mini_truck.png')
ambulance_image = pygame.image.load('images/small/Ambulance/Ambulance.png')
police_image = pygame.image.load('images/small/Police/Police.png')
taxi_image = pygame.image.load('images/small/taxi/taxi.png')
mini_van_image = pygame.image.load('images/small/Mini_van/Mini_van.png')
black_viper_image = pygame.image.load('images/small/Black_viper/Black_viper.png')

