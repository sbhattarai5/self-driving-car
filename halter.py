from init import *


class Halter:
    def __init__(self):
        pass

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
