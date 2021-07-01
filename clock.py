from helper_functions import *
from surface import *

def draw_clock():
    time = round(pygame.time.get_ticks() / 1000.0, 2)
    time = "Time (secs): " + str(time)
    time = FONT48.render(time, True, WHITE)
    surface = SingletonSurface.getInstance().surface
    surface.blit(time, (1000, 0))
    
