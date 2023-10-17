
from turtle import Screen
import turtle as t

import random
tim = t.Turtle()
tim.shape('turtle')
tim.color("lime")
#tim.pensize(10)
tim.speed(0)
t.colormode(255)

# def make_a_square(size):
#     """draws a square with the size parameter being the length you want to move forwards"""
#     for i in range(4):
#         tim.fd(size)
#         tim.lt(90)

#make_a_square(100)
# for i in range(15):
#     tim.pendown()
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)

colors = ["red","orange","yellow","green","blue","indigo","violet","pink","lime","black"]

# def make_a_shape(sides):
#     "draws a shape with n as the number of sides, and color as its color"
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

## we run through 10 numbers from 3 to 10 cause 11 is non exclusive. Then for each iteration we set tims color to a random choice from
## the list colors that we made above. then we run the function make a shape with the number of sides being the current number the iterator is on.
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     make_a_shape(i)

# make_a_shape(3,"red")
# make_a_shape(4,"orange")
# make_a_shape(5,"yellow")
# make_a_shape(6,"green")
# make_a_shape(7,"blue")
# make_a_shape(8,"indigo")
# def movement_process(): 
#     movement = [tim.left(90),tim.right(90)]

#     #tim.forward(25)
#     #tim.left(90)
#     lor = random.choice(movement)
    
#     tim.forward(25)
#     lor
#     #tim.backward(25)
# def progress():
#     movement = [tim.fd(25),tim.back(25)]
#     return random.choice(movement)

# for i in range(11):
#     tim.color(random.choice(colors))
#     movement_process()
#     #progress()

# movement = [tim.left(90),tim.right(90)]
# lor = random.choice(movement)
# for i in range(4):
#     tim.left(90)
#     tim.forward(100)
#     tim.forward(-100)
#     #tim.left(-90)


#directions holds the directions for east, north west and south
directions= [0,90,180,270]

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)

#we move tim 30 paces forwards and with the setheading method it takes a random choice from our list and sets the turtle to
#point in that direction, then when the loop iterates the turtle starts off moving in that direction!
# for i in range(200):
#     tim.color(random_color())
#     choice = random.choice(directions)
#     tim.forward(30)
#     tim.setheading(choice)

for i in range(360):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(200)



            
    
















#this code creates the screen we use and keeps it open until we click it close.
##needs to happen after all our code so we keep it on the bottom of the script.
screen = Screen()
screen.exitonclick()
