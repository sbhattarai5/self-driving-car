from helper_functions import *
from surface import *
import pygame
from config import *
from viewwindow import *

# Creates a clock class
# Values include a surface to draw on and an x,y coordinate for drawing


class Clock:
    def __init__(self, x, y):
        viewwindow = SingletonViewWindow.get_instance()
        self.x, self.y = viewwindow.transform(x, y)

    # Method for getting the time
    def get_time(self):
        return round(pygame.time.get_ticks() / 1000.0, 2)

    # Method for drawing the time on the surface.
    def run(self):
        surface = SingletonSurface.getInstance().surface
        # viewwindow = SingletonViewWindow.get_instance()

        time = self.get_time()
        time = "Time (secs): " + str(time)
        time = FONT48.render(time, True, WHITE)

        surface.blit(time, (self.x, self.y))


# Not a method within the class, just a function for creating the clock
def create_clock():
    return Clock(ROAD_X + ((NUM_LANES + 1) * LANE_WIDTH), 17)
