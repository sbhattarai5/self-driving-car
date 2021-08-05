import sys, math
from surface import *
from helper_functions import *
from config import *
import random

random.seed()
from viewwindow import *
from road import *
from divider import *
from vehicle import *

# Sensor Class for the Car


# Sensor Class for the Car
class Sensor:
    def __init__(self, w, h):
        self.w = w
        self.h = h
<<<<<<< Updated upstream
        self.nearbyObjects = []
=======
<<<<<<< Updated upstream
=======
        self.center_x, self.center_y = None, None
        self.nearbyObjects = []
>>>>>>> Stashed changes
        # self.rect = pygame.Rect(x, y, w, h)
>>>>>>> Stashed changes
        surface = SingletonSurface.getInstance().surface

    def get_distance(self, audi, obj):
        x1, y1 = get_center(audi)
        x2, y2 = get_center(obj)
        return math.sqrt(abs((pow(x1 - x2, 2) + pow(y1 - y2, 2))))

    def detectWorld(self, audi, WorldObjects):
        viewwindow = SingletonViewWindow.get_instance()
        surface = SingletonSurface.getInstance().surface
<<<<<<< Updated upstream
        self.nearbyObjects = []

=======
<<<<<<< Updated upstream
        nearby_objects =[]
=======
        self.center_x, self.center_y = get_center(audi)
>>>>>>> Stashed changes
        self.nearbyObjects = []
>>>>>>> Stashed changes
        #############################################################
        # Detects the grass for the audi
        if audi.x < ROAD_X + (LANE_WIDTH):
            # Detects the Grass on the Left
            self.nearbyObjects.append(
                (
                    "GRASS",
<<<<<<< Updated upstream
                    ROAD_X,
                    audi.y - (audi.h / PIXEL),
                    1 / PIXEL,
=======
                    ROAD_X - self.center_x,
                    audi.y - (audi.h / PIXEL) - self.center_y,
                    2 / PIXEL,
>>>>>>> Stashed changes
                    audi.h / PIXEL,
                    False,
                )
            )

        if audi.x > ROAD_X + (LANE_WIDTH * (NUM_LANES - 1)):
            # Detects the Grass on the Right when in range
            self.nearbyObjects.append(
                (
                    "GRASS",
<<<<<<< Updated upstream
                    ROAD_X + (LANE_WIDTH * NUM_LANES),
                    audi.y - (audi.h / PIXEL),
                    1 / PIXEL,
=======
                    ROAD_X + (LANE_WIDTH * NUM_LANES) - self.center_x,
                    audi.y - (audi.h / PIXEL) - self.center_y,
                    2 / PIXEL,
>>>>>>> Stashed changes
                    audi.h / PIXEL,
                    False,
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
            self.nearbyObjects.append(
                (
                    "GRASS",
<<<<<<< Updated upstream
                    audi.x,
                    audi.y - (audi.h / PIXEL),
=======
                    ROAD_X - self.center_x,
                    audi.y - (audi.h / PIXEL) - self.center_y,
>>>>>>> Stashed changes
                    1 / PIXEL,
                    audi.h / PIXEL,
                    True,
                )
            )

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
                        self.nearbyObjects.append(
                            (
                                "CAR",
<<<<<<< Updated upstream
                                obj.x,
                                obj.y - obj.h / (PIXEL),
=======
                                obj.x - self.center_x,
                                obj.y - obj.h / (PIXEL) - self.center_y,
>>>>>>> Stashed changes
                                obj.w / PIXEL,
                                obj.h / PIXEL,
                                True,
                            )
                        )
                        # Return label and rectangle of object and let the sim decide if it needs to stop
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
                    if colliderect(mrect, rect) == False:
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
                     #Adds the car object to sensed list
                        self.nearbyObjects.append(("CAR",obj.x, obj.y - obj.h/(PIXEL), obj.w/PIXEL, obj.h/PIXEL, False))
                    nearby_objects.append(("CAR", obj.x, obj.y, False))
                
=======
>>>>>>> Stashed changes
                        # Adds the car object to sensed list
                        self.nearbyObjects.append(
                            (
                                "CAR",
<<<<<<< Updated upstream
                                obj.x,
                                obj.y - obj.h / (PIXEL),
=======
                                obj.x - self.center_x,
                                obj.y - obj.h / (PIXEL) - self.center_y,
>>>>>>> Stashed changes
                                obj.w / PIXEL,
                                obj.h / PIXEL,
                                False,
                            )
                        )
<<<<<<< Updated upstream

=======
                    nearby_objects.append(("CAR", obj.x, obj.y, False))

>>>>>>> Stashed changes
>>>>>>> Stashed changes
            elif isinstance(obj, RoadModel):
                for div in obj.dividers:
                    if self.get_distance(audi, div) <= MAX_RADIUS:
                        self.nearbyObjects.append(
<<<<<<< Updated upstream
                            ("Divider", div.x, div.y, div.w, div.h, False)
=======
                            (
                                "Divider",
                                div.x - self.center_x,
                                div.y - self.center_y,
                                div.w,
                                div.h,
                                False,
                            )
>>>>>>> Stashed changes
                        )


####


class SensorView:
    def __init__(self, sensor):
        self.sensor = sensor

    def run(self):
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        for obj in self.sensor.nearbyObjects:
<<<<<<< Updated upstream
            rect = viewwindow.transform_rect(obj[1], obj[2], obj[3], obj[4])
=======
            rect = viewwindow.transform_rect(
                obj[1] + self.sensor.center_x,
                obj[2] + self.sensor.center_y,
                obj[3],
                obj[4],
            )
>>>>>>> Stashed changes
            pygame.draw.rect(surface, RED, rect, 2)
