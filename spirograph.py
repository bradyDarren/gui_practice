import turtle as t 
import random as r 

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")

def rand_color():
    red = r.randint(0,255)
    blue = r.randint(0,255)
    green = r.randint(0,255)
    random_color = (red,blue,green)
    return random_color     

def change_position(): 
    current_pos = tim.heading()
    tim.setheading(current_pos + 10)

for _ in range(200): 
    tim.color(rand_color())
    tim.circle(100,360,200)
    change_position()
    


screen = t.Screen()
screen.exitonclick()

