import sys, math
from surface import *
from helper_functions import *
from config import *
import random; random.seed()
from viewwindow import *
from road import *
from divider import *
from vehicle import *

#Sensor Class for the Car



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
        return(math.sqrt(abs((pow(x1 - x2, 2) +
                              pow(y1 - y2, 2)))))
    
    def detectWorld(self,audi, WorldObjects):
        viewwindow = SingletonViewWindow.get_instance()
        surface = SingletonSurface.getInstance().surface
        nearby_objects =[]
        self.nearbyObjects = []
        
        #############################################################
        #Detects the grass for the audi
        if audi.x < ROAD_X + (LANE_WIDTH):
            #Detects the Grass on the Left
            self.nearbyObjects.append(("GRASS",ROAD_X, audi.y-(audi.h/PIXEL), 1/PIXEL, audi.h/PIXEL, False))
           
        if audi.x > ROAD_X + (LANE_WIDTH * (NUM_LANES - 1)):
            #Detects the Grass on the Right when in range
            self.nearbyObjects.append(("GRASS", ROAD_X +(LANE_WIDTH * NUM_LANES), audi.y-(audi.h/PIXEL), 1/PIXEL, audi.h/PIXEL, False))
            
        
        if audi.x < ROAD_X or audi.x > ROAD_END:
            print("<Car,", round(audi.x),", ", round(audi.y),
                  ", ", audi.w, ", ", audi.h, "> collides with GRASS")
            self.nearbyObjects.append(("GRASS", audi.x, audi.y-(audi.h/PIXEL), 1/PIXEL, audi.h/PIXEL, True))
            
        
        #########################################################################################
        #This now senses the other objects in the world and adds them to the nearby objects list
        for obj in WorldObjects:
            #Try to move the if-else using inheritance.
            #Computes the distance
           
            if isinstance(obj, VehicleModel):
                 if self.get_distance(audi, obj) < MAX_RADIUS and self.get_distance(audi, obj) > 0:
                    #Sensor code for cars
                    rect = (obj.x, obj.y, obj.w/PIXEL, obj.h/PIXEL)
                    mrect = (audi.x, audi.y, audi.w/PIXEL, audi.h/PIXEL)
                    if colliderect(mrect, rect):
                        self.nearbyObjects.append(("CAR",obj.x, obj.y - obj.h/(PIXEL), obj.w/PIXEL, obj.h/PIXEL, True))
                        #Return label and rectangle of object and let the sim decide if it needs to stop
                        print("<Car,", round(audi.x),", ", round(audi.y),
                  ", ", audi.w, ", ", audi.h, "> collides with CAR")
                        #sys.exit()
                    if colliderect(mrect, rect) == False:
                     #Adds the car object to sensed list
                        self.nearbyObjects.append(("CAR",obj.x, obj.y - obj.h/(PIXEL), obj.w/PIXEL, obj.h/PIXEL, False))
                    nearby_objects.append(("CAR", obj.x, obj.y, False))
                
            elif isinstance(obj, RoadModel):
                for div in obj.dividers:
                    if self.get_distance(audi, div) <= MAX_RADIUS:
                        self.nearbyObjects.append(("Divider", div.x, div.y, div.w, div.h, False))
####
    
class SensorView:
    def __init__(self, sensor):
        self.sensor = sensor

    def run(self):
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        for obj in self.sensor.nearbyObjects:
            rect = viewwindow.transform_rect(obj[1], obj[2], obj[3], obj[4])
            pygame.draw.rect(surface, RED, rect, 2)

