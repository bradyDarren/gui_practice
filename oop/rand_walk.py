# will make our turtle icon generate a random path to walk, while changing color and thickness of the paths as a different direction is taken. 

from turtle import Turtle, Screen
import random

t = Turtle()
t.color("green")
t.shape("turtle")

colors = ["spring green", "cornflower blue", "gold", "deep pink", "crimson"]

""" 1. generate a random color."""
def rand_color():
    color = random.choice(colors)
    return color 

"""function created to make sure we account for each directional movement passed into our turtle object."""

def right(name):
    name.right(90)

def left(name):
    name.left(90)

def forward(name):
    name.forward(10)

def backward(name):
    name.backward(10)

""" 2. generate a random direction to move (right/left/forward/backward),  """

options = [right, left, forward, backward]

def rand_direct(choices):
    selection = random.choice(options)
    return selection()

rand_direct(options)

""" 3. Increase line thickness as each move is made. As well as change color of the line as each move is made. """


"""test line for the scren display"""
screen = Screen()
screen.exitonclick()

