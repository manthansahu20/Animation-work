import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colors = [(255,0,0),(255,20,147),(255,105,180),(255,182,193)]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.begin_fill()
    t.left(50)
    t.forward(50)
    t.circle(25, 200)
    t.right(140)
    t.circle(25, 200)
    t.forward(50)
    t.left(50)
    t.end_fill()
    t.right(10)

turtle.done()
