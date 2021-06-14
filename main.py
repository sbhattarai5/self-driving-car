from factory import *

carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects = factory()
while (1):

    starttime = pygame.time.get_ticks()

    halter.run()

    roadcontrol.run(WorldObjects)
    audicontrol.run()
    carcontrol.run()
    viewwindow.run()

    ########################################
    
    draw_grass()
    roadview.run()
    carmodel.sensor.detectWorld(carmodel, WorldObjects)
    carview.run()
    audiview.run()
    pygame.display.flip()

    # create an object called FramerateControl. Replace the following codes with
    # frameratecontrol.run()
    
    # delaying Frames. TO-DO: Add this to our halter class, very easy to do, should take 5 minutes.
    delay = get_delay(starttime)
    if delay > 0:
        pygame.time.delay(delay)

    
