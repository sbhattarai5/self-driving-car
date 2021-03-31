from init import *
from helper_functions import *

dividers = get_dividers()

def draw_road():
    pygame.draw.rect(surface, ROAD_COLOR, road_rect)
    for divider in dividers:
        pygame.draw.rect(surface, DIVIDER_COLOR, divider)

