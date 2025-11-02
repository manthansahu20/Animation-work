import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["white", "cyan", "magenta", "blue", "violet"]

for i in range(150):
    t.pencolor(random.choice(colors))
    t.forward(i * 2 / 3)
    t.right(45)
    t.circle(i / 2, 30)
    t.right(60)

t.hideturtle()
turtle.done()
