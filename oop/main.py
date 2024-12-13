import turtle
from icon import Icon
from rand_walk import Colors, RandDirection, Line

icon_name = input("Input the desired name of you icon: ")
icon_color = input("Input the desired color of your icon: ")
icon_shape = input("Input the desired shape of your icon (arrow/turtle/circle/square/triangle/classic): ")

"""passing in the responses from the user."""
user_icon = Icon(icon_name, icon_color, icon_shape)

"""assigning the user input for name and assigning it to a Turtle() object."""
user_icon.name = turtle.Turtle()

"""passing in the user input to designate the shape and color of our Turle() object. """
user_icon.name.shape(icon_shape)
user_icon.name.color(icon_color)

user_icon.name.speed(10)

# user_icon.name.right(90)

path = RandDirection(user_icon.name)
line = Line()
colors = Colors()

turtle.colormode(255)

for _ in range(250):
    path.rand_direct()
    user_icon.name.forward(25)
    user_icon.name.pencolor(colors.rand_color())
    user_icon.name.pensize(line.thickness())

screen = turtle.Screen()
screen.exitonclick()
