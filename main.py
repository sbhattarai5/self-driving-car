import sys
import random; random.seed()
import pygame
from init import *
from road import *
from vehicle import *
from clock import *

car_x = road_rect[0] + LANE_WIDTH/2
car_y = 450
car_dx = 0
car_dy = 1

audi_x = road_rect[0] + 3 * LANE_WIDTH/2
audi_y = 500
audi_dx = 0
audi_dy = -0.2
audi_angle = 0

dy = 1  # check if I can comment this


while 1:

    starttime = pygame.time.get_ticks()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ## maybe
    # variables = [car_x, car_y, audi_dx, audi_dy]
    # manipulate_key(keys, variables)
    ##############
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 0.1
    elif keys[pygame.K_RIGHT]:
        car_x += 0.1
    elif keys[pygame.K_UP]:
        dy += 0.1
    elif keys[pygame.K_DOWN]:
        dy -= 0.1
    elif keys[pygame.K_r]:
        # Test rotation
        audi_angle = (audi_angle + 10) % 360
        audi_image = pygame.image.load('images/small/Audi/Audi-%s.png' % audi_angle)
            
    for i in range(len(dividers)):
        dividers[i].y += dy
    if dividers[0].y >= DIVIDER_HEIGHT:
        d = dividers.pop()
        d.y = -DIVIDER_HEIGHT + (dividers[0].y - DIVIDER_HEIGHT)
        dividers.insert(0, d)

    # random speed change
    car_y += dy
    r = random.randrange(100) 
    if r == 1:
        audi_dy += 0.05
    elif r == 2:
        audi_dy -= 0.05
        
    audi_x, audi_y = move_vehicle(audi_x, audi_y, audi_dx, audi_dy)

    # drawing
    draw_grass()
    draw_road()
    draw_vehicle(car_image, car_x, car_y)
    draw_vehicle(audi_image, audi_x, audi_y)
    draw_vehicle(mini_truck_image, 500, 200)
    draw_vehicle(ambulance_image, 550, 200)
    draw_vehicle(police_image, 600, 200)
    draw_vehicle(taxi_image, 650, 200)
    draw_vehicle(black_viper_image, 700, 200)
    draw_vehicle(mini_van_image, 750, 200)
    draw_clock()
    pygame.display.flip()
    
    # delaying
    delay = get_delay(starttime)
    if delay > 0:
        pygame.time.delay(delay)
