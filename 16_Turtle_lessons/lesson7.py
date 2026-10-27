
import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

screen = turtle.Screen()


# Draw grass
t.penup()
t.goto(-350, -150)
t.pendown()
t.color("green")
t.pensize(5)
t.forward(700)
t.pensize(2)

# Function to draw one flower
def flower(x, y, color):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()

    # Green stem
    t.color("green")
    t.forward(70)

    # Flower petals
    t.color(color)

    for i in range(6):
        t.circle(15)
        t.left(60)

    # Flower center
    t.penup()
    t.goto(x, y + 70)
    t.dot(18, "orange")

# Draw three flowers
flower(-150, -150, "pink")
flower(0, -150, "purple")
flower(150, -150, "red")

t.hideturtle()
turtle.done()
