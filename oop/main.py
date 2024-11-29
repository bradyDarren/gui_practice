from turtle import Turtle, Screen
from icon import Icon
from rand_walk import
import random 

icon_name = input("Input the desired name of you icon: ")
icon_color = input("Input the desired color of your icon: ")
icon_shape = input("Input the desired shape of your icon (arrow/turtle/circle/square/triangle/classic): ")

user_icon = Icon(icon_name, icon_color, icon_shape)

user_icon.name = Turtle()

user_icon.name.shape(icon_shape)
user_icon.name.color(icon_color)



screen = Screen()
screen.exitonclick()
