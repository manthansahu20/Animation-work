import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

colors = [(255,0,0),(255,192,203),(255,255,0),(0,255,255),(0,128,0),(0,0,255)]

for i in range(12):
    t.pencolor(colors[i % len(colors)])
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(100 - i*5)
    t.right(30)

turtle.done()
