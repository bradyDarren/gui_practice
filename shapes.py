# creation of multiple shapes - triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, and decagon

from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("blue")

tom.penup()
tom.goto(0,200)
tom.pendown()

for i in range(3,11):
    degrees = 360/i
    for _ in range(i):
        tom.forward(150)
        tom.right(degrees)

screen = Screen()
screen.exitonclick()