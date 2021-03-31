from init import *

def get_dividers():
    x = road_rect.x + road_rect.w/2 - divider_width / 2
    dividers = [pygame.Rect(x, i, DIVIDER_WIDTH, DIVIDER_HEIGHT) for i in range(-(DIVIDER_HEIGHT + DIVIDER_SPACING), 1000, DIVIDER_HEIGHT + DIVIDER_SPACING)]
    return dividers

def draw(image, cx, cy, draw_bounding_box=True, draw_larger_bounding_box=False):
    # The cx,cy is center of rect for blit
    w, h = image.get_size()
    x = cx - w/2
    y = cy - h/2
    surface.blit(image, (x, y))
    # draw bounding box
    if draw_bounding_box:
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        pygame.draw.rect(surface, RED, rect, 1)
    # draw tighter bounding box
    if draw_larger_bounding_box:
        rect.x = x - 20
        rect.y = y - 20
        rect.w += 40
        rect.h += 40
        pygame.draw.rect(surface, RED, rect, 4)


def get_delay(starttime):
    endtime = pygame.time.get_ticks()
    delay  = int(MILLISEC_PER_FRAME - (endtime - starttime))
    return delay
