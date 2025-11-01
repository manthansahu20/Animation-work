import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colors = [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(148,0,211)]

for i in range(72):
    t.pencolor(colors[i % len(colors)])
    for _ in range(4):
        t.forward(100 - i)
        t.right(90)
    t.right(5)

turtle.done()
