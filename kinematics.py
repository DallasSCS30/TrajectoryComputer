##----------------------------------------------------------------------
## Kinematics Module
## Dallas Spendelow
## October 3, 2018
## This module contains some functions for evaluating kinematic equations.
##----------------------------------------------------------------------

def position(initPos,vel,accel,time):
    resultPos = initPos + vel*time+0.5*accel*time**2
    return resultPos

def velocity(initVel,accel,time):
    resultVel = initVel + accel*time
    return resultVel

def time(initVel,finalVel,accel):
    resultTime = (finalVel - initVel)/accel
    return resultTime
    