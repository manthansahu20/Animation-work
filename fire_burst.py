import turtle
import random

# Create screen and set background color
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

# Use color names instead of RGB tuples
colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

for i in range(36):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.forward(100)
    t.backward(100)
    t.right(10)

turtle.done()
