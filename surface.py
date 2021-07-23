from init import *


class SingletonSurface:
    class __Surface:
        def __init__(self):
            self.surface = pygame.display.set_mode(SIZE)

    # static member
    __instance = __Surface()

    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def getInstance():
        """TODO: return the surface itself"""
        return SingletonSurface.__instance
