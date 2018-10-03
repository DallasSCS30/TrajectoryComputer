##-------------------------------------------------------------------
## Trajectories
## Dallas Spendelow
## October 3, 2018
## This program computes trajectories. Future versions may give the 
## user the ability to set gravitational acceleration, as well as the
## ability to choose the output quantities (position vs. velocity).
## The program is currently hardcoded to output position. 
##-------------------------------------------------------------------

import output
import kinematics
import math


## Ask the user for some inputs.
InitVel = float(input("Input the initial velocity. "))
angleDegrees = float(input("At what angle? "))


## Do some math/physics with the inputs.

timeStep = 0.1          ## How far each iteration steps forward in time (seconds).
                        ## A smaller number will be more accurate.

angleRadians = angleDegrees/180*3.1415

VelX = InitVel*math.cos(angleRadians)      ## Recall that horizontal velocity is
                                           ## constant in projectile motion.

InitVelY = InitVel*math.sin(angleRadians)

InitXpos = 0
InitYpos = 0

VelY = InitVelY


## Main loop. The program will update position components and velocity
## components to step forward in time.

import plot

aboveGround = True

while(aboveGround):
    if InitYpos < 0:
        aboveGround = False
    Xpos = kinematics.position(InitXpos,VelX,0,timeStep)
    Ypos = kinematics.position(InitYpos,VelY,-9.8,timeStep)

    VelY = kinematics.velocity(VelY,-9.8,timeStep)

    plot.point(Xpos,Ypos)
    output.printComponents(Xpos,Ypos)
    
    InitXpos = Xpos
    InitYpos = Ypos