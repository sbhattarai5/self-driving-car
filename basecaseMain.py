from basecaseFactory import *


carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects, clock = (
    factory()
)
while 1:

    halter.update()
    halter.run()

    carcontrol.run()
    viewwindow.run()
    roadcontrol.run(WorldObjects)
    audicontrol.run()

    ########################################

    roadview.run()
    carmodel.sensor.detectWorld(carmodel, WorldObjects)
    carview.run()
    audiview.run()

    clock.run()

    pygame.display.flip()

    # create an object called FramerateControl. Replace the following codes with
    # frameratecontrol.run()

    # delaying
    halter.delay()
