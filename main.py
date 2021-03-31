import sys
import random; random.seed()
import pygame
from config import *

frame_rate = 30.0
millisec_per_frame = 1000.0/frame_rate

surface = pygame.display.set_mode(SIZE)

# dividers height 40, space 40
divider_width = 10
x = road_rect.x + road_rect.w/2 - divider_width / 2
dividers = [pygame.Rect(x, i, DIVIDER_WIDTH, DIVIDER_HEIGHT) for i in range(-(DIVIDER_HEIGHT + DIVIDER_SPACING), 1000, DIVIDER_HEIGHT + DIVIDER_SPACING)]

car_image = pygame.image.load('images/small/Car/Car.png')
car_image = pygame.image.load('images/small/Black_viper/Black_viper.png')
car_x = road_rect[0] + LANE_WIDTH/2
car_y = 450
car_dy = 0.0

audi_image = pygame.image.load('images/small/Audi/Audi.png')
audi_x = road_rect[0] + 3 * LANE_WIDTH/2
audi_y = 500
audi_dy = -0.2
audi_angle = 0

mini_truck_image = pygame.image.load('images/small/Mini_truck/Mini_truck.png')
ambulance_image = pygame.image.load('images/small/Ambulance/Ambulance.png')
police_image = pygame.image.load('images/small/Police/Police.png')
taxi_image = pygame.image.load('images/small/taxi/taxi.png')
mini_van_image = pygame.image.load('images/small/Mini_van/Mini_van.png')
black_viper_image = pygame.image.load('images/small/Black_viper/Black_viper.png')

dy = 1

def draw(surface, image, cx, cy, draw_bounding_box=True, draw_larger_bounding_box=False):
    # The cx,cy is center of rect for blit
    w, h = image.get_size()
    x = cx - w/2
    y = cy - h/2
    surface.blit(image, (x, y))
    # draw bounding box
    if draw_bounding_box:
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        pygame.draw.rect(surface, RED, rect, 1)
    # draw tighter bounding box
    if draw_larger_bounding_box:
        rect.x = x - 20
        rect.y = y - 20
        rect.w += 40
        rect.h += 40
        pygame.draw.rect(surface, RED, rect, 4)


while 1:

    starttime = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
    audi_y += audi_dy
    
    surface.fill(GRASS_COLOR)
    pygame.draw.rect(surface, ROAD_COLOR, road_rect)
    for divider in dividers:
        pygame.draw.rect(surface, DIVIDER_COLOR, divider)

    draw(surface, car_image, car_x, car_y)
    draw(surface, audi_image, audi_x, audi_y)

    # Test some images
    draw(surface, mini_truck_image, 500, 200)
    draw(surface, ambulance_image, 550, 200)
    draw(surface, police_image, 600, 200)
    draw(surface, taxi_image, 650, 200)
    draw(surface, black_viper_image, 700, 200)
    draw(surface, mini_van_image, 750, 200)
    
    time = round(pygame.time.get_ticks() / 1000.0, 2)
    time = "Time (secs): " + str(time)
    time = FONT48.render(time, True, WHITE)
    surface.blit(time, (1000, 0))
    
    pygame.display.flip()

    endtime = pygame.time.get_ticks()
    delay  = int(millisec_per_frame - (endtime - starttime))
    if delay > 0:
        pygame.time.delay(delay)
