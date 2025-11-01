import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.width(2)

colors = [(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130),(148,0,211)]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    for _ in range(2):
        t.circle(100,60)
        t.left(120)
    t.right(10)

turtle.done()
