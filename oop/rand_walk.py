# will make our turtle icon generate a random path to walk, while changing color and thickness of the paths as a different direction is taken. 

# from turtle import Turtle, Screen
import random

# t = Turtle()
# t.color("green")
# t.shape("turtle")


""" 1. generate a random color. Enabling us to change the color of our line with each move."""
class Colors:
    color_choice = ["spring green", "cornflower blue", "gold", "deep pink", "crimson"]

    def rand_color(self):
        color = random.choice(self.color_choice)
        return color 

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

    def right(self):
        self.turtle.right(90)

    def left(self):
        self.turtle.left(90)

    def forward(self):
        self.turtle.forward(25)

    def backward(self):
        self.turtle.backward(25)
            
    def rand_direct(self):
        self.options = [
            self.right,
            self.left,
            self.forward,
            self.backward
        ]
        prev_selection = None
        """ The function is designed to ensure that if 'left' is selected, the next choice cannot be 'right' or 'left' again.
        Only 'forward' or 'backward' are allowed as the subsequent options. """
        while True:
            selection = random.choice(self.options)
            if prev_selection in [self.right, self.left] and selection in [self.right, self.left]:
                continue

            prev_selection = selection    
            return selection()

"""test line for the scren display"""
# screen = Screen()
# screen.exitonclick()

