
import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.title("Spiral Stars")
screen.bgcolor("black")
screen.setup(800, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

# Star colors
colors = [
   
	"#B27BFF","#FF4BED"	,"#FF8DCF",
    "#1EC5B4"	,"#76FAFA","#F9FAFC"

]

# Function to draw a filled star
def draw_star(size, color):
    t.color(color,color)
    t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()

# Draw spiral stars
for i in range(45):
    angle = i * 25
    radius = i * 6

    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    size = 15 + i * 0.6
    color = colors[i % len(colors)]

    draw_star(size, color)

# Add a title
t.penup()
t.goto(0, 300)
t.color("white")
t.write(
    "SPIRAL STARS",
    align="center",
    font=("Arial", 24, "bold")
)

screen.exitonclick()
