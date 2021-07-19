import sys, math
from surface import *
from helper_functions import *
from config import *
import random

random.seed()
from viewwindow import *
from road import *
from time import time


def get_center(obj):
    x = obj.x - (obj.w / (PIXEL)) / 2
    y = obj.y - (obj.h / PIXEL) / 2
    return x, y


# Sensor Class for the Car
class Sensor:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        # self.rect = pygame.Rect(x, y, w, h)
        surface = SingletonSurface.getInstance().surface

    def get_distance(self, audi, obj):
        x1, y1 = get_center(audi)
        x2, y2 = get_center(obj)
        return math.sqrt(abs((pow(x1 - x2, 2) + pow(y1 - y2, 2))))

    def detectWorld(self, audi, WorldObjects):
        viewwindow = SingletonViewWindow.get_instance()
        surface = SingletonSurface.getInstance().surface
        nearby_objects = []
        self.nearbyObjects = []

        #############################################################
        # Detects the grass for the audi
        if audi.x < ROAD_X + (LANE_WIDTH):
            # Detects the Grass on the Left
            nearby_objects.append(("GRASS", ROAD_X, audi.y))
            self.nearbyObjects.append(
                (ROAD_X, audi.y - (audi.h / PIXEL), 1 / PIXEL, audi.h / PIXEL)
            )

        if audi.x > ROAD_X + (LANE_WIDTH * (NUM_LANES - 1)):
            # Detects the Grass on the Right when in range
            nearby_objects.append(("GRASS", ROAD_X + (LANE_WIDTH * NUM_LANES), audi.y))
            self.nearbyObjects.append(
                (
                    ROAD_X + (LANE_WIDTH * NUM_LANES),
                    audi.y - (audi.h / PIXEL),
                    1 / PIXEL,
                    audi.h / PIXEL,
                )
            )

        if audi.x < ROAD_X or audi.x > ROAD_END:
            print(
                "<Car,",
                round(audi.x),
                ", ",
                round(audi.y),
                ", ",
                audi.w,
                ", ",
                audi.h,
                "> collides with GRASS",
            )
            nearby_objects.append(("GRASS", ROAD_X, audi.y, True))
            # sys.exit()

        #########################################################################################
        # This now senses the other objects in the world and adds them to the nearby objects list
        for obj in WorldObjects:
            # Try to move the if-else using inheritance.
            # Computes the distance

            if isinstance(obj, VehicleModel):
                if (
                    self.get_distance(audi, obj) < MAX_RADIUS
                    and self.get_distance(audi, obj) > 0
                ):
                    # Sensor code for cars
                    rect = (obj.x, obj.y, obj.w / PIXEL, obj.h / PIXEL)
                    mrect = (audi.x, audi.y, audi.w / PIXEL, audi.h / PIXEL)
                    if colliderect(mrect, rect):

                        # Return label and rectangle of object and let the sim decide if it needs to stop
                        nearby_objects.append(("CAR", obj.x, obj.y, True))
                        print(
                            "<Car,",
                            round(audi.x),
                            ", ",
                            round(audi.y),
                            ", ",
                            audi.w,
                            ", ",
                            audi.h,
                            "> collides with CAR",
                        )
                        # sys.exit()

                    # Adds the car object to sensed list
                    self.nearbyObjects.append(
                        (obj.x, obj.y - obj.h / (PIXEL), obj.w / PIXEL, obj.h / PIXEL)
                    )
                    nearby_objects.append(("CAR", obj.x, obj.y, False))

            elif isinstance(obj, RoadModel):
                for div in obj.dividers:
                    if self.get_distance(audi, div) <= MAX_RADIUS:
                        self.nearbyObjects.append((div.x, div.y, div.w, div.h))


####


class SensorView:
    def __init__(self, Sensor):
        self.sensor = Sensor

    def run(self):
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        for obj in self.sensor.nearbyObjects:
            rect = viewwindow.transform_rect(obj[0], obj[1], obj[2], obj[3])
            pygame.draw.rect(surface, RED, rect, 2)


class VehicleModel:
    def __init__(
        self, image, position, speed, accelaration, target_speed, max_speed, car_type
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
