# drawing a square. 

from turtle import Turtle, Screen

timmy = Turtle() 
timmy.color("red")
timmy.shape("turtle")

for _ in range(4):
    timmy.forward(200)
    timmy.right(90)



screens = Screen()
screens.exitonclick()