
import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

screen = turtle.Screen()
turtle.colormode(255)

# House body
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("black", "#B4E29A")
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.left(90)

t.end_fill()

# Roof
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()
t.goto(0, 180)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Door
t.penup()
t.goto(-25, -100)
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()

for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

# Left window
t.penup()
t.goto(-80, 0)
t.pendown()
t.color("black", "lightblue")
t.begin_fill()

for i in range(4):
    t.forward(40)
    t.left(90)

t.end_fill()

# Right window
t.penup()
t.goto(40, 0)
t.pendown()
t.begin_fill()

for i in range(4):
    t.forward(40)
    t.left(90)

t.end_fill()

# Door handle
t.penup()
t.goto(15, -60)
t.pendown()
t.dot(7, "yellow")

# Sun
t.penup()
t.goto(140, 140)
t.pendown()
t.color("orange", "yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# Green ground
t.penup()
t.goto(-300, -105)
t.pendown()
t.color("green")
t.pensize(5)
t.forward(600)

t.hideturtle()
turtle.done()
