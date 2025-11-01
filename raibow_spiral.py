import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colors = [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(148,0,211)]

for i in range(150):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 2)
    t.left(59)

turtle.done()
