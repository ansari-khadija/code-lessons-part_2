import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw a circle on the left
t.color("blue")
t.penup()
t.goto(-200, 0)
t.pendown()
t.circle(50)


# Draw a triangle in the middle
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("green")

for i in range(3):
    t.forward(100)
    t.left(120)

# Draw a square on the right
t.penup()
t.goto(100, 0)
t.pendown()
t.color("red")

for i in range(4):
    t.forward(100)
    t.left(90)

t.hideturtle()
turtle.done()
