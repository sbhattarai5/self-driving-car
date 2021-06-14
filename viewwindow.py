from init import *

class ViewWindow:

    def __init__(self, carmodel):
        '''
        world_x = world's camera's origin
        view_x = top left of camera's position in the surface
        '''
        self.carmodel = carmodel
        self.world_x = None
        self.world_y = None
        self.run()
        self.world_w = WORLD_W
        self.world_h = WORLD_H
        self.view_x = VIEW_X
        self.view_y = VIEW_Y
        self.view_w = VIEW_W
        self.view_h = VIEW_H

    def transform(self, wx, wy):
        vx = ((wx - self.world_x) / self.world_w) * self.view_w + self.view_x
        vy = -(((wy - self.world_y) / self.world_h) * self.view_h - self.view_y - self.view_h)
        return (vx, vy)

    def transform_rect(self, rx, ry, rw, rh):
        vx, vy = self.transform(rx, ry + rh)
        vw, vh = rw * self.view_w / self.world_w, rh * self.view_h / self.world_h
        vrect = pygame.Rect(vx, vy, vw, vh)
        return vrect

    def run(self): 
        self.world_x = self.carmodel.x - 22
        self.world_y = self.carmodel.y - 17.6
        

class SingletonViewWindow:
    __instance = None
    
    def __init__(self):
        raise NotImplementedError
    
    @staticmethod
    def set_instance(viewwindow):
        SingletonViewWindow.__instance = viewwindow

    @staticmethod
    def get_instance():
        return SingletonViewWindow.__instance
