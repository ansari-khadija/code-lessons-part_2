
import turtle

t = turtle.Turtle()
t.pensize(2)

colors = [
    "red", "blue",
    "purple", "orange",
    "green", "magenta"
]

for i in range(6):
    t.color(colors[i % len(colors)])
    t.circle(50)
    t.left(60)
   

turtle.done()
