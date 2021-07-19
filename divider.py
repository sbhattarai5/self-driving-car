from config import *
from surface import *
from viewwindow import *


class divider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = DIVIDER_WIDTH
        self.h = DIVIDER_HEIGHT
        self.color = DIVIDER_COLOR

    def draw(self):
        surface = SingletonSurface.getInstance().surface
        viewwindow = SingletonViewWindow.get_instance()
        r = viewwindow.transform_rect(self.x, self.y, self.w, self.h)

        pygame.draw.rect(surface, self.color, r)
