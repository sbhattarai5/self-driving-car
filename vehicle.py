import sys, math
from surface import *
from helper_functions import *
from config import *
import random

random.seed()
from viewwindow import *
from road import *
from time import time

# Sensor Class for the Car
class Sensor:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        # self.rect = pygame.Rect(x, y, w, h)
        surface = SingletonSurface.getInstance().surface

    def get_distance(self, audi, obj):
        viewwindow = SingletonViewWindow.get_instance()
        # audi_x, audi_y = viewwindow.transform(audi.x, audi.y)
        if isinstance(obj, VehicleModel):
            return math.sqrt(abs((pow(audi.x - obj.x, 2) + pow(audi.y - obj.y, 2))))
        else:
            return math.sqrt(abs((pow(audi.x - obj[0], 2) + pow(audi.y - obj[1], 2))))

    def detectWorld(self, audi, WorldObjects):
        viewwindow = SingletonViewWindow.get_instance()
        surface = SingletonSurface.getInstance().surface
        # USEFUL CONSTANTS FOR COMPUTATION
        # road_end = viewwindow.transform(ROAD_END, 0)
        # road_x = viewwindow.transform(ROAD_X, 0)
        x, y = viewwindow.transform(audi.x, audi.y)
        nearby_objects = []

        #############################################################
        # Detects the grass for the audi
        if audi.x < ROAD_X + (LANE_WIDTH):
            # Detects the Grass on the Left
            nearby_objects.append(("GRASS", ROAD_X, audi.y))
            rect = viewwindow.transform_rect(
                ROAD_X, audi.y - (audi.h / PIXEL), 1 / PIXEL, audi.h / PIXEL
            )
            pygame.draw.rect(surface, RED, rect, 1)

        if audi.x > ROAD_X + (LANE_WIDTH * (NUM_LANES - 1)):
            # Detects the Grass on the Right when in range
            nearby_objects.append(("GRASS", ROAD_X + (LANE_WIDTH * NUM_LANES), audi.y))
            rect = viewwindow.transform_rect(
                ROAD_X + LANE_WIDTH * NUM_LANES,
                audi.y - (audi.h / PIXEL),
                1 / PIXEL,
                audi.h / PIXEL,
            )
            pygame.draw.rect(surface, RED, rect, 1)

        # If the car is in the grass, end the sim
        if audi.x < ROAD_X or audi.x > ROAD_END:
            print("ON GRASS")
            sys.exit()
        ################################################
        #########################################################################################
        # This now senses the other objects in the world and adds them to the nearby objects list
        for obj in WorldObjects:
            # Computes the distance
            if isinstance(obj, VehicleModel):
                if (
                    self.get_distance(audi, obj) < MAX_RADIUS
                    and self.get_distance(audi, obj) > 0
                ):
                    # Sensor code for cars
                    obj.draw_bounding_box = True
                    # print(obj.draw_bounding_box)
                    rect = (obj.x, obj.y, obj.w / PIXEL, obj.h / PIXEL)

                    mrect = (audi.x, audi.y, audi.w / PIXEL, audi.h / PIXEL)
                    # Write own function for this TO_DO
                    if colliderect(mrect, rect):
                        # print("Collided, Stop Sim")
                        # This works now. If two cars collide, it stops the sim
                        sys.exit()
                    # Adds the car object to sensed list
                    nearby_objects.append(("CAR", obj.x, obj.y))
                else:
                    obj.draw_bounding_box = False
            # World Objects will have roadmodel in it instead of list of dividers
            elif isinstance(obj, RoadModel):
                for div in obj.dividers:
                    if abs(div[0] - audi.x) > MAX_RADIUS:
                        continue
                    else:
                        if self.get_distance(audi, div) < MAX_RADIUS:
                            x, y = div[0], div[1]
                            nearby_objects.append(("DIVIDER", div[0], div[1]))
                            rect = viewwindow.transform_rect(x, y, div[2], div[3])
                            pygame.draw.rect(surface, RED, rect, 5)

        #############################################################################


## road.py
def draw_grass():
    surface = SingletonSurface.getInstance().surface
    surface.fill(GRASS_COLOR)


class VehicleModel:
    def __init__(
        self,
        image,
        position,
        speed,
        accelaration,
        target_speed,
        max_speed,
        car_type,
        draw_bounding_box=False,
        draw_larger_bounding_box=False,
    ):
        self.image = image
        self.position = position
        self.speed = speed
        self.accelaration = accelaration
        self.target_speed = target_speed
        self.max_speed = max_speed
        self.accelaration_depression = 0.0
        self.w, self.h = image.get_size()
        self.sensor = Sensor(self.w, self.h)
        self.car_type = car_type
        self.draw_bounding_box = draw_bounding_box
        self.draw_larger_bounding_box = draw_larger_bounding_box
        self.last_time = time()

    def get_x(self):
        return self.position[0]

    def set_x(self, x):
        self.position[0] = x

    def get_y(self):
        return self.position[1]

    def set_y(self, y):
        self.position[1] = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def run(self):
        raise NotImplementedError

    def move_instantly(self, vect):
        self.position += vect

    def move(self):
        target_speed = self.accelaration_depression * self.max_speed
        current_time = time()
        delta_t = current_time - self.last_time

        if target_speed[1] > self.speed[1]:
            self.speed += self.accelaration * delta_t
        elif target_speed[1] < self.speed[1]:
            self.speed -= self.accelaration * delta_t

        self.position += self.speed * delta_t
        self.x, self.y = self.position
        self.last_time = current_time

    def set_accelaration_depression(self, accelaration_depression):
        self.accelaration_depression = accelaration_depression


class VehicleControlUser:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vehiclemodel.move_instantly((-0.1, 0))
        elif keys[pygame.K_RIGHT]:
            self.vehiclemodel.move_instantly((0.1, 0))
        elif keys[pygame.K_UP]:
            self.vehiclemodel.accelaration_depression = max(
                self.vehiclemodel.accelaration_depression + 0.01, 1.0
            )
        elif keys[pygame.K_DOWN]:
            self.vehiclemodel.accelaration_depression = min(
                self.vehiclemodel.accelaration_depression - 0.01, 0.0
            )
        self.vehiclemodel.move()


class VehicleControlRandom:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        r = random.randrange(40)
        if r == 1:
            self.vehiclemodel.set_accelaration_depression(
                self.vehiclemodel.accelaration_depression + 0.1
            )
        elif r == 2:
            self.vehiclemodel.set_accelaration_depression(
                self.vehiclemodel.accelaration_depression - 0.1
            )
        self.vehiclemodel.move()


class VehicleView:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        x, y = self.vehiclemodel.position
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        x, y = viewwindow.transform(x, y)

        surface.blit(self.vehiclemodel.image, (x, y))
        # draw bounding box

        if self.vehiclemodel.draw_bounding_box:
            rect = self.vehiclemodel.image.get_rect()
            rect.x = x
            rect.y = y
            pygame.draw.rect(surface, RED, rect, 1)
        # draw tighter bounding box
        if self.vehiclemodel.draw_larger_bounding_box:
            rect.x = x - 20
            rect.y = y - 20
            rect.w += 40
            rect.h += 40
            pygame.draw.rect(surface, RED, rect, 4)
