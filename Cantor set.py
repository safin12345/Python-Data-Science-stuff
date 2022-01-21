#Plot cantor fractor set
from turtle import *

def cantor(x,y,length):
    if length>=5:
        speed(1) # Fastest speed when speed(0)
        penup()
        pensize(3)
        pencolor('red')
        setpos(x , y)
        pendown()
        fd(length)
        y-= 30
        cantor(x,y,length / 3)
        cantor(x+2 * length / 3 , y , length / 3)
        penup()
        setpos(x , y + 30)
