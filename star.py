import turtle
import random

# setup screen
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "white"]

# draw multiple rotating stars
for i in range(36):
    t.pencolor(random.choice(colors))
    
    # draw one star
    for j in range(5):
        t.forward(150)
        t.right(144)
    
    # rotate a bit for next star
    t.right(10)

t.hideturtle()
turtle.done()
