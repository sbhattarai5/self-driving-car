import pygame, sys
from helper_functions import *
from config import *

#Creates a class with Surface(For Drawing the clock), as well as x, y coordinates(For Positioning)
class Clock:
    #Initialize Function
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
    #Function to get the time
    def get_time(self):
        return round(pygame.time.get_ticks() / 1000.0, 2)
    #Function to draw the time
    def draw_clock():
        time = self.get_time()
        time = "Time (secs): " + str(time)
        time = FONT48.render(time, True, WHITE)
        self.surface.blit(time, (self.x, self.y))
    
