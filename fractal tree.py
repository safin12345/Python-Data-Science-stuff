# A colour fractal tree
from turtle import *
setheading(90)
penup()
setpos(0 , -250)
pendown()
def fractal_tree_color(length , level):
    pensize(length / 10)
    if length < 20:
        pencolor('green') # Green leaves.
    else:
        pencolor('brown') # Trunk and branches.
    speed(0)

    if level > 0:
        fd(length)
        rt(30)
        fractal_tree_color(length * 0.7 , level -1)
        lt(90)
        fractal_tree_color(length * 0.5, level - 1)
        rt(60)
        penup()
        bk(length) # Backwards
        pendown()
    
        
        
