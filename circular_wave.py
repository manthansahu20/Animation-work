import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(100 + 50 * math.sin(math.radians(i * 3)))
    t.right(1)

turtle.done()
