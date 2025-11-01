import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
colors = [(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255)]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.right(10)

turtle.done()
