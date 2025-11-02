import turtle

# Create a screen object and set background color
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

# Use color names (Trinket doesn't support RGB tuples)
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.circle(50 + i * 5)
    t.right(10)

turtle.done()
