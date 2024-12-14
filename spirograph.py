import turtle as t 
import random as r 

tim = t.Turtle()
t.colormode(255)

def rand_color():
    red = r.randint(0,255)
    blue = r.randint(0,255)
    green = r.randint(0,255)
    random_color = (red,blue,green)
    return random_color

tim.circle(100,360)
tim.color(rand_color())


screen = t.Screen()
screen.exitonclick()

