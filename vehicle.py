from init import *
from helper_functions import *

def draw_vehicle(car_image, car_x, car_y):
    draw(car_image, car_x, car_y)

def move_vehicle(car_x, car_y, dx, dy):
    car_x += dx
    car_y += dy
    return car_x, car_y

## road.py
def draw_grass():
    surface.fill(GRASS_COLOR)
    
    
    
