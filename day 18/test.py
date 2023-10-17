from turtle import Screen, Turtle
import random
tim = Turtle()
tim.shape('turtle')
tim.color("lime")
# tim.pensize(10)
tim.speed(0)
colors = ["red","orange","yellow","green","blue","indigo","violet","pink","lime","black"]
directions= ["right", "left", "up", "down"]


# for i in range(500):
#     tim.color(random.choice(colors))
#     choice = random.choice(directions)
    
#     if choice == "right":
#         tim.forward(25)
#     elif choice == "left":
#         tim.backward(25)
#     elif choice == "up":
#         tim.left(90)
#         tim.forward(25)
#         tim.right(90)
#     elif choice == "down":
#         tim.right(90)
#         tim.forward(25)
#         tim.left(90)

for i in range(360):
    tim.setheading(i)
    tim.circle(100)




screen = Screen()
screen.exitonclick()
