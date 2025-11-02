import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")

star = turtle.Turtle()
star.speed(0)
star.color("yellow")
star.hideturtle()

# draw falling stars
for i in range(30):
    star.penup()
    star.goto(random.randint(-200, 200), random.randint(100, 250))
    star.pendown()
    for j in range(5):
        star.forward(20)
        star.right(144)
    time.sleep(0.1)
    star.clear()

turtle.done()
