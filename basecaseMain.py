from basecaseFactory import *


<<<<<<< Updated upstream
carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects, clock = (
    factory()
)
=======
<<<<<<< Updated upstream
carmodel, carcontrol, carview, audimodel, audicontrol, audiview, roadmodel, roadcontrol, roadview, viewwindow, halter, WorldObjects, sensorView, clock = (
    factory()
)
=======
(
    carmodel,
    carcontrol,
    carview,
    audimodel,
    audicontrol,
    audiview,
    roadmodel,
    roadcontrol,
    roadview,
    viewwindow,
    halter,
    WorldObjects,
    sensorView,
    clock,
) = factory()
surface = SingletonSurface.getInstance().surface
>>>>>>> Stashed changes
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
    sensorView.run()
>>>>>>> Stashed changes
    carview.run()
    audiview.run()

    clock.run()

    pygame.display.flip()

    # create an object called FramerateControl. Replace the following codes with
    # frameratecontrol.run()

    # delaying
    halter.delay()
