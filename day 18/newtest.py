
from turtle import Screen
import turtle as t

import random
tim = t.Turtle()
tim.shape('turtle')
tim.color("lime")
#tim.pensize(10)
tim.speed(0)
t.colormode(255)





def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)



for i in range(0,360,5):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)