
import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(2)

colors = ["red", "blue", "green", "orange"]

for i in range(36):
    t.color(colors[i % 4])
    t.forward(190)
    t.right(100)
    t.right(10)

turtle.done()
