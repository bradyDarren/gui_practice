from turtle import Turtle, Screen

tim = Turtle() 
tim.shape("turtle")
tim.color("green")

# tim.forward(50)
# # tim.penup(10)

for _ in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()


my_screen = Screen() 
my_screen.exitonclick()
    