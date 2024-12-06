from turtle import Turtle, Screen
from icon import Icon
from rand_walk import Colors, RandDirection

icon_name = input("Input the desired name of you icon: ")
icon_color = input("Input the desired color of your icon: ")
icon_shape = input("Input the desired shape of your icon (arrow/turtle/circle/square/triangle/classic): ")

"""passing in the responses from the user."""
user_icon = Icon(icon_name, icon_color, icon_shape)

"""assigning the user input for name and assigning it to a Turtle() object."""
user_icon.name = Turtle()

"""passing in the user input to designate the shape and color of our Turle() object. """
user_icon.name.shape(icon_shape)
user_icon.name.color(icon_color)

user_icon.name.speed(1)

# user_icon.name.right(90)

path = RandDirection(user_icon.name)

for _ in range(250):
   path.rand_direct()

screen = Screen()
screen.exitonclick()
