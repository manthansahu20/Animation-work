import turtle
import math
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Color list
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

# Draw pattern
for i in range(720):
    t.pencolor(colors[i % len(colors)])        # Cycle through colors
    t.forward(100 + 50 * math.sin(math.radians(i * 4)))
    t.right(61)                                # Angle for spiral twist
    t.forward(50)
    t.right(59)

# Hide the turtle and finish
t.hideturtle()
turtle.done()
