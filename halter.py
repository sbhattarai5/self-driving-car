from init import *
from helper_functions import *

class Halter:

    def __init__(self):
        self.starttime = pygame.time.get_ticks()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self):
        self.starttime = pygame.time.get_ticks()

    def delay(self):
        delay = get_delay(self.starttime)
        if delay > 0:
            pygame.time.delay(delay)
