
import turtle

t = turtle.Turtle()

colors = ["red", "green", "blue", "yellow", "orange"]
t.speed(0)
t.pensize(2)

for i in range(100):
    t.color(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(80)

turtle.done()
