import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

colors = [(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255)]

for i in range(36):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.forward(100)
    t.backward(100)
    t.right(10)

turtle.done()
