from factory import *

carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects = (
    factory()
)
count = 0
while 1:
    count = count + 1

    starttime = pygame.time.get_ticks()

    halter.run()

    carcontrol.run()
    viewwindow.run()
    roadcontrol.run(WorldObjects)
    audicontrol.run()

    ########################################

    draw_grass()
    roadview.run()
    carmodel.sensor.detectWorld(carmodel, WorldObjects)
    carview.run()
    audiview.run()
    pygame.display.flip()

    # create an object called FramerateControl. Replace the following codes with
    # frameratecontrol.run()

    # delaying
    delay = get_delay(starttime)
    if delay > 0:
        pygame.time.delay(delay)

    # print("Road: ", roadmodel.road_x, roadmodel.road_y, roadmodel.road_height)
    # print("Car: ", carmodel.x, carmodel.y)
    # temp = input("Enter something: ")
