from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
tim.pencolor("pink")

a=0
b=0
tim.speed(0)
tim.penup()
tim.goto(0,200)
tim.pendown()
while True:
    tim.forward(a)
    tim.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    tim.hideturtle()

screen.exitonclick()