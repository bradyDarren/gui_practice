# will make our turtle icon generate a random path to walk, while changing color and thickness of the paths as a different direction is taken. 

from turtle import Turtle, Screen
import random

# t = Turtle()
# t.color("green")
# t.shape("turtle")


""" 1. generate a random color."""
class Colors:
    color_choice = ["spring green", "cornflower blue", "gold", "deep pink", "crimson"]

    def rand_color(self):
        color = random.choice(self.color_choice)
        return color 

"""function created to make sure we account for each directional movement passed into our turtle object."""
class Directions:
    name = ""

    def right(self):
        self.name.right(90)

    def left(self, name):
        name.left(90)

    def forward(self, name):
        name.forward(200)

    def backward(self, name):
        name.backward(200)

""" 2. generate a random direction to move (right/left/forward/backward),  """
class RandDirection:
    options = [Directions.right, Directions.left, Directions.forward, Directions.backward]

    def rand_direct(self, choices):
        selection = random.choice(choices)
        return selection()

""" 3. Increase line thickness as each move is made. As well as change color of the line as each move is made. """


"""test line for the scren display"""
# screen = Screen()
# screen.exitonclick()

