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
    x = obj.x - (obj.w /(PIXEL))/ 2
    y = obj.y - (obj.h / PIXEL)/2
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
            nearby_objects.append(("GRASS", ROAD_X, audi.y))
            self.nearbyObjects.append((ROAD_X, audi.y-(audi.h/PIXEL), 1/PIXEL, audi.h/PIXEL))
           
        if audi.x > ROAD_X + (LANE_WIDTH * (NUM_LANES - 1)):
            #Detects the Grass on the Right when in range
            nearby_objects.append(("GRASS", ROAD_X +(LANE_WIDTH  * NUM_LANES), audi.y ))
            self.nearbyObjects.append((ROAD_X +(LANE_WIDTH * NUM_LANES), audi.y-(audi.h/PIXEL), 1/PIXEL, audi.h/PIXEL))
            
        
        if audi.x < ROAD_X or audi.x > ROAD_END:
            print("<Car,", round(audi.x),", ", round(audi.y),
                  ", ", audi.w, ", ", audi.h, "> collides with GRASS")
            nearby_objects.append(("GRASS", ROAD_X, audi.y, True))
            #sys.exit()
        
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
                        
                        #Return label and rectangle of object and let the sim decide if it needs to stop
                        nearby_objects.append(("CAR", obj.x, obj.y, True))
                        print("<Car,", round(audi.x),", ", round(audi.y),
                  ", ", audi.w, ", ", audi.h, "> collides with CAR")
                        #sys.exit()
                        
                    #Adds the car object to sensed list
                    self.nearbyObjects.append((obj.x, obj.y - obj.h/(PIXEL), obj.w/PIXEL, obj.h/PIXEL))
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
        self,
        image,
        x,
        y,
        dx,
        dy,
        ddx,
        ddy,
        target_dx,
        target_dy,
        max_dy,
        angle,
        car_type,
    ):
        self.image = image
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy
        self.target_dx = target_dx
        self.target_dy = target_dy
        self.max_dy = max_dy
        self.accn_depression = 0.0
        self.w, self.h = image.get_size()
        self.sensor = Sensor(self.w, self.h)
        self.angle = angle
        self.car_type = car_type
        self.last_time = time()

    def run(self):
        raise NotImplementedError

    def move_instantly(self, dx=None, dy=None):
        if dx == None:
            dx = self.dx
        if dy == None:
            dy = self.dy
        self.x += dx
        self.y += dy

    def change_accelaration(self, dddx, dddy):
        self.ddx += dddx
        self.ddy += dddy

    def change_velocity(self, ddx, ddy):
        self.dx += ddx
        self.dy += ddy

    def rotate(self):
        self.angle = (self.angle + 10) % 360
        self.image = pygame.image.load(
            "images/small/"
            + self.car_type
            + "/"
            + self.car_type
            + "-%s.png" % self.angle
        )

    def move(self):
        # change velocity
        self.target_dy = self.accn_depression * self.max_dy

        current_time = time()
        delta_t = current_time - self.last_time

        if self.target_dy > self.dy:
            self.dy += self.ddy * delta_t
        if self.target_dy < self.dy:
            self.dy -= self.ddy * delta_t

        self.x += self.dx * delta_t
        self.y += self.dy * delta_t

        self.last_time = current_time

    def set_accelaration(self, ddx, ddy):
        self.ddx = ddx
        self.ddy = ddy


class VehicleControlUser:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vehiclemodel.move_instantly(-0.1, 0)
        elif keys[pygame.K_RIGHT]:
            self.vehiclemodel.move_instantly(0.1, 0)
        elif keys[pygame.K_UP]:
            self.vehiclemodel.accn_depression = max(
                self.vehiclemodel.accn_depression + 0.1, 1.0
            )
        elif keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_r]:
            self.vehiclemodel.rotate()
        else:
            self.vehiclemodel.accn_depression = 0
        self.vehiclemodel.move()


class VehicleControlRandom:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        r = random.randrange(40)
        if r == 1:
            self.vehiclemodel.change_velocity(0, 0.1)
        elif r == 2:
            self.vehiclemodel.change_velocity(0, -0.1)
        self.vehiclemodel.move_instantly()


class VehicleView:
    def __init__(self, vehiclemodel):
        self.vehiclemodel = vehiclemodel

    def run(self):
        x = self.vehiclemodel.x
        y = self.vehiclemodel.y
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        x, y = viewwindow.transform(x, y)
        # print(x, y)

        surface.blit(self.vehiclemodel.image, (x, y))
        # draw bounding box

