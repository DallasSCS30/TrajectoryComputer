##-------------------------------------------------------------------
## Output Module
## Dallas Spendelow
## October 3, 2018
## This module outputs data in text format.
##-------------------------------------------------------------------

## This function outputs quantities such as position, velocity, and
## acceleration. It outputs both horizontal and vertical components
## in a text format. 

def printComponents(x,y):       
    print(x,",",y)
    
## This function outputs only the magnitude of the chosen quantity.

def printMagnitude(x):
    print(x)