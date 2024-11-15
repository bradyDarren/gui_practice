# will make our turtle icon generate a random path to walk, while changing color and thickness of the paths as a different direction is taken. 

from turtle import Turtle, Screen

t = Turtle()
t.color("green")
t.shape("turtle")

colors = ["spring green", "cornflower blue", "gold", "deep pink", "crimson"]

""" 1. generate a random color."""
random.choice(colors)
""" 2. generate a random direction to move (right/left/forward/backward),  """

""" 3. Increase line thickness as each move is made. As well as change color of the line as each move is made. """




screen = Screen()
screen.exitonclick()

