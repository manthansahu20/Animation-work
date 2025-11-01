import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colors = [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(75,0,130)]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.circle(50 + i*5)
    t.right(10)

turtle.done()
