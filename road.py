from init import *
from surface import *
from helper_functions import *
from viewwindow import *


class RoadModel:
    def __init__(self, carmodel,
                 num_lanes = NUM_LANES, lane_width = LANE_WIDTH,
                 road_height = ROAD_HEIGHT, road_color = ROAD_COLOR,
                 divider_width = divider_width, DIVIDER_WIDTH = DIVIDER_WIDTH, divider_height = DIVIDER_HEIGHT,
                 divider_spacing = DIVIDER_SPACING, divider_color = DIVIDER_COLOR,
                 size = SIZE):
        self.carmodel = carmodel
        self.size = size
        
        #lanes
        self.num_lanes = num_lanes
        self.lane_width = lane_width
        
        #road
        self.road_x = self.carmodel.x
        self.road_y = self.carmodel.y 
        self.road_color = road_color
        self.road_height = road_height
        self.road = (self.road_x, self.road_y, self.num_lanes * self.lane_width, self.road_height)
        
        #dividers
        self.divider_width = divider_width
        self.DIVIDER_WIDTH = DIVIDER_WIDTH
        self.divider_height = divider_height
        self.divider_spacing = divider_spacing
        self.divider_color = divider_color
        self.dividers = []

        
        

class RoadControl:
    def __init__(self, road, dy = 0.2):
        self.road_model = road
        self.dy = dy

    def setDividers(self):
        #setDividers:
        self.road_model.dividers = []
        
        x = self.road_model.road[0] + LANE_WIDTH * 0 - self.road_model.divider_width / 2
        start_y = int(self.road_model.carmodel.y) - 17
    
        remainder = start_y % (self.road_model.divider_height + self.road_model.divider_spacing)

        #divider
        if (remainder <= self.road_model.divider_height):
            start_y = start_y - remainder
        else: #space
            start_y = start_y + remainder 

            
        start_y = int(start_y)
        for i in range(1, NUM_LANES):
            x += LANE_WIDTH

            for y in range(start_y, start_y + 37, self.road_model.divider_height + self.road_model.divider_spacing):
                #viewwindow = SingletonViewWindow.get_instance()
                #r = viewwindow.transform_rect(x, y, self.road_model.DIVIDER_WIDTH, self.road_model.divider_height)
                r = (x, y, self.road_model.DIVIDER_WIDTH, self.road_model.divider_height)
                self.road_model.dividers.append(r)


    def runRoad(self):
        self.road_model.road_y = self.road_model.carmodel.dy + self.road_model.carmodel.y - 17.6
        self.road_model.road = (self.road_model.road_x, self.road_model.road_y, self.road_model.num_lanes * self.road_model.lane_width, self.road_model.road_height)
        

    def runDividers(self, worldObjects):
        
        self.setDividers()
        for divider in self.road_model.dividers:
            worldObjects.append(divider)

    def run(self, worldObjects):
        self.runRoad()
        self.runDividers(worldObjects)
        
        
        

            
class RoadView:
    def __init__(self, road):
        self.road_model = road
        
    def run(self):
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        vrect = viewwindow.transform_rect(self.road_model.road[0], self.road_model.road[1], self.road_model.road[2], self.road_model.road[3])
        pygame.draw.rect(surface, self.road_model.road_color, vrect)
        
        for divider in self.road_model.dividers:
            r = viewwindow.transform_rect(divider[0], divider[1], divider[2], divider[3])
            pygame.draw.rect(surface, self.road_model.divider_color, r)

