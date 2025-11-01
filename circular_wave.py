import turtle
import math

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

colors = [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130)]

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(100 + 50 * math.sin(math.radians(i*3)))
    t.right(1)

turtle.done()
