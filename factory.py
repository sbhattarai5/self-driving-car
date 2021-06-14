'''
   manufactures all the objects needed for the simulation
'''

import sys
from road import *
from vehicle import *
from clock import *
from halter import *

def factory():
    car_x = road_rect[0] + LANE_WIDTH/2
    print ("car_x: ", car_x)
    #car_y = 450
    car_y = 13
    car_dx = 0
    car_dy = 0.2
    car_angle = 0

    audi_x = car_x + 19.5
    audi_y = car_y
    audi_dx = 0
    audi_dy = 0.2
    audi_angle = 0

    carmodel = VehicleModel(car_image, car_x, car_y, car_dx, car_dy, car_angle, 'Black_viper')
    carcontrol = VehicleControlUser(carmodel)
    carview = VehicleView(carmodel)
    audimodel = VehicleModel(audi_image, audi_x, audi_y, audi_dx, audi_dy, audi_angle, 'Audi')
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
    return carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects
    
