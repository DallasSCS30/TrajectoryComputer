##-------------------------------------------------------------------
## Plot Module
## Dallas Spendelow
## October 3, 2018
## This module plots the output trajectory using turtle graphics.
##-------------------------------------------------------------------

import turtle

## The turtle module is used to draw the trajectory, by simply
## going to the calculated points.

spot = turtle.Turtle()
window = turtle.Screen()
spot.goto(0,0)
spot.color("black")
spot.down()

def point(x,y):
    spot.goto(x,y)
    

