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
    x = obj.x + (obj.w / (PIXEL)) / 2
    y = obj.y - (obj.h / PIXEL) / 2
    return x, y


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
        has_sensor=False,
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
        if has_sensor:
            self.sensor = Sensor(self.w, self.h)
        else:
            self.sensor = None

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
<<<<<<< Updated upstream

    def move_instantly(self, vect):
        self.position += vect

=======

    def move_instantly(self, vect):
        self.position += vect

>>>>>>> Stashed changes
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


from sensor import *


class VehicleControlUser:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def keepCenter(self):
        objects = self.vehiclemodel.sensor.nearbyObjects
        x1, y1 = get_center(self.vehiclemodel)
        leftDistance = MAX_RADIUS + 1
        rightDistance = MAX_RADIUS
        for obj in objects:
            if obj[1] + obj[3] > self.vehiclemodel.x - x1 and not (obj[0] == "CAR"):
                x2 = obj[1]
                distance = math.sqrt(abs((pow(0 - x2, 2) + pow(y1 - y1, 2))))
                if distance < leftDistance:
                    leftDistance = distance

            if obj[1] < self.vehiclemodel.x + (
                self.vehiclemodel.w / PIXEL
            ) - x1 and not (obj[0] == "CAR"):
                x2 = obj[1] + obj[3]
                distance = math.sqrt(abs((pow(0 - x2, 2) + pow(y1 - y1, 2))))
                if distance < rightDistance:
                    rightDistance = distance
        if round(leftDistance, 2) < round(rightDistance, 2):
            self.vehiclemodel.move_instantly((-0.01, 0))
        elif round(leftDistance, 2) > round(rightDistance, 2):
            self.vehiclemodel.move_instantly((0.01, 0))

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
<<<<<<< Updated upstream
            if self.vehiclemodel.speed[1] != 0:
                self.vehiclemodel.move_instantly((-0.1, 0))
        elif keys[pygame.K_RIGHT]:
            if self.vehiclemodel.speed[1] != 0:
                self.vehiclemodel.move_instantly((0.1, 0))
=======
            self.vehiclemodel.move_instantly((-0.1, 0))
        elif keys[pygame.K_RIGHT]:
            self.vehiclemodel.move_instantly((0.1, 0))
>>>>>>> Stashed changes
        elif keys[pygame.K_UP]:
            self.vehiclemodel.accelaration_depression = max(
                self.vehiclemodel.accelaration_depression + 0.01, 1.0
            )
        elif keys[pygame.K_DOWN]:
            self.vehiclemodel.accelaration_depression = min(
                self.vehiclemodel.accelaration_depression - 0.01, 0.0
            )
<<<<<<< Updated upstream
=======
        self.keepCenter()
>>>>>>> Stashed changes
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
        if vehiclemodel.sensor == None:
            self.sensorView = None
        else:
            self.sensorView = SensorView(vehiclemodel.sensor)

    def run(self):
        x, y = self.vehiclemodel.position
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        x, y = viewwindow.transform(x, y)

<<<<<<< Updated upstream
=======
        if self.sensorView != None:
            self.sensorView.run()
>>>>>>> Stashed changes
        surface.blit(self.vehiclemodel.image, (x, y))
<<<<<<< Updated upstream
        if self.sensorView != None:
            self.sensorView.run()
=======
>>>>>>> Stashed changes
