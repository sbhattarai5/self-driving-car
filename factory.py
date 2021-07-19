"""
   manufactures all the objects needed for the simulation
"""

import sys
from road import *
from vehicle import *
from clock import *
from halter import *
from clock import *


def vect2(x, y):
    return pygame.math.Vector2(x, y)


def factory():
    car_x = road_rect[0] + LANE_WIDTH / 2
    car_y = 13
    car_position = vect2(car_x, car_y)
    car_dx = 0
    car_dy = 0
    car_speed = vect2(car_dx, car_dy)
    car_ddx = 0
    car_ddy = 2
    car_accelaration = vect2(car_ddx, car_ddy)
    car_target_dx = 0
    car_target_dy = 0
    car_target_speed = vect2(car_target_dx, 0)
    car_max_dx = 0
    car_max_dy = 50
    car_max_speed = vect2(car_max_dx, car_max_dy)
    car_angle = 0

    audi_x = car_x + 19.5
    audi_y = car_y
    audi_position = vect2(audi_x, audi_y)
    audi_dx = 0
    audi_dy = 0.2
    audi_speed = vect2(audi_dx, audi_dy)
    audi_ddx = 0
    audi_ddy = 2
    audi_accelaration = vect2(audi_ddx, audi_ddy)
    audi_target_dx = 0
    audi_target_dy = 0
    audi_target_speed = vect2(audi_target_dx, audi_target_dy)
    audi_max_dx = 0
    audi_max_dy = 50
    audi_max_speed = vect2(audi_max_dx, audi_max_dy)
    audi_angle = 0

    carmodel = VehicleModel(
        car_image,
        car_position,
        car_speed,
        car_accelaration,
        car_target_speed,
        car_max_speed,
        "Black_viper",
    )
    carcontrol = VehicleControlUser(carmodel)
    carview = VehicleView(carmodel)
    audimodel = VehicleModel(
        audi_image,
        audi_position,
        audi_speed,
        audi_accelaration,
        audi_target_speed,
        audi_max_speed,
        "Audi",
    )
    audicontrol = VehicleControlRandom(audimodel)
    audiview = VehicleView(audimodel)
    WorldObjects = []
    WorldObjects.append(audimodel)
    WorldObjects.append(carmodel)
    viewwindow = ViewWindow(carmodel)
    SingletonViewWindow.set_instance(viewwindow)

    roadmodel = RoadModel(carmodel)
    WorldObjects.append(roadmodel)
    roadcontrol = RoadControl(roadmodel)
    roadview = RoadView(roadmodel)
    sensorView = SensorView(carmodel.sensor)
    halter = Halter()
    clock = create_clock()
    return (
        carmodel,
        carcontrol,
        carview,
        audimodel,
        audicontrol,
        audiview,
        roadmodel,
        roadcontrol,
        roadview,
        viewwindow,
        halter,
        WorldObjects,
        sensorView,
        clock
    )
