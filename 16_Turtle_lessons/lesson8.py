
import turtle

# Screen setup
screen = turtle.Screen()
screen.title("My Beautiful Drawing")
screen.bgcolor("ivory")
screen.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Ask for your name
name = screen.textinput("Your Name", "Enter your name:")


# Function to draw grass
def draw_grass():
    t.penup()
    t.goto(-400, -150)
    t.setheading(0)
    t.pendown()

    t.color("green", "lightgreen")
    t.begin_fill()

    for i in range(2):
        t.forward(800)
        t.right(90)
        t.forward(150)
        t.right(90)

    t.end_fill()


# Function to draw a flower
def flower(x, y, color):
    # Draw stem
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()

    t.color("green")
    t.forward(120)

    # Draw six petals
    t.color("black", color)

    for i in range(6):
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        t.left(60)

    # Draw flower center
    t.penup()
    t.goto(x, y + 120)
    t.dot(25, "orange")


# Function to draw the sun
def draw_sun():
    t.penup()
    t.goto(220, 150)
    t.setheading(0)
    t.pendown()

    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(45)
    t.end_fill()


# Draw the grass
draw_grass()

# Draw two flowers
flower(-180, -150, "pink")
flower(100, -150, "purple")

# Draw the sun
draw_sun()

# Write your name at the top
t.penup()
t.goto(0, 220)
t.color("darkblue")

if name:
    message = "Welcome, " + name + "!"
else:
    message = "My Beautiful Drawing"

t.write(
    message,
    align="center",
    font=("Arial", 26, "bold")
)

# Hide turtle and finish
t.hideturtle()
screen.exitonclick()
