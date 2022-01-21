# Koch curve fractal.

from turtle import *

def koch_curve(length , stage):
    speed(0)
    if stage == 0:
        fd(length)
        return
    koch_curve(length / 3, stage - 1)
    lt(60)
    koch_curve(length / 3, stage - 1)
    rt(120)
    koch_curve(length / 3, stage - 1)
    lt(60)
    koch_curve(length / 3, stage - 1)
    
    
