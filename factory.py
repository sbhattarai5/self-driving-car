"""
   manufactures all the objects needed for the simulation
"""

import sys
from road import *
from vehicle import *
from clock import *
from halter import *


def factory():
    car_x = road_rect[0] + LANE_WIDTH / 2
    car_y = 13
    car_dx = 0
    car_dy = 0
    car_ddx = 0
    car_ddy = 2
    car_target_dx = 0
    car_max_dy = 50
    car_target_dy = 0
    car_angle = 0

    audi_x = car_x + 19.5
    audi_y = car_y
    audi_dx = 0
    audi_dy = 0.2
    audi_ddx = 0
    audi_ddy = 2
    audi_target_dx = 0
    audi_target_dy = 0
    audi_max_dy = 50
    audi_angle = 0

    carmodel = VehicleModel(
        car_image,
        car_x,
        car_y,
        car_dx,
        car_dy,
        car_ddx,
        car_ddy,
        car_target_dx,
        car_target_dy,
        car_max_dy,
        car_angle,
        "Black_viper",
    )
    carcontrol = VehicleControlUser(carmodel)
    carview = VehicleView(carmodel)
    audimodel = VehicleModel(
        audi_image,
        audi_x,
        audi_y,
        audi_dx,
        audi_dy,
        audi_ddx,
        audi_ddy,
        audi_target_dx,
        audi_target_dy,
        audi_max_dy,
        audi_angle,
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
    halter = Halter()
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
    )
