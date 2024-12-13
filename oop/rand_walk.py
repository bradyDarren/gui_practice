# will make our turtle icon generate a random path to walk, while changing color and thickness of the paths as a different direction is taken. 

# from turtle import Turtle, Screen
import random

# t = Turtle()
# t.color("green")
# t.shape("turtle")

""" 1. generate a random color. Enabling us to change the color of our line with each move."""
class Colors:

    def rand_color(self):
        red = random.randint(0,255)
        blue = random.randint(0,255)
        green = random.randint(0,255)
        random_color = (red,blue,green)
        return random_color

""" 2. Increase line thickness as each move is made."""
class Line: 

    linesize = .5

    def thickness(self):
        if self.linesize < 20:
            self.linesize += .2
            return self.linesize
        else: 
            return self.linesize


""" 3. generate a random direction to move (right/left/forward/backward),  """
"""function created to make sure we account for each directional movement passed into our turtle object."""
class RandDirection:

    def __init__(self, turtle):
        self.turtle = turtle

    def north(self):
        self.turtle.setheading(0)

    def south(self):
        self.turtle.setheading(180)

    def east(self):
        self.turtle.setheading(90)

    def west(self):
        self.turtle.setheading(270)
            
    def rand_direct(self):
        self.options = [
            self.north,
            self.south,
            self.east,
            self.west
        ]
        # prev_selection = None
        """ The function is designed to ensure that if 'left' is selected, the next choice cannot be 'right' or 'left' again.
        Only 'forward' or 'backward' are allowed as the subsequent options. """
        selection = random.choice(self.options)
        return selection()
    

"""test line for the scren display"""
# screen = Screen()
# screen.exitonclick()

