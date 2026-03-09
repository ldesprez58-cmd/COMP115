import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# Draw Sky (Top Half)

t.penup()
t.goto(-400, 0)
t.pendown()
t.color("orange")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.left(90)
    t.forward(300)
    t.left(90)
t.end_fill()


# Draw Ocean (Bottom Half)
t.penup()
t.goto(-400, -300)
t.pendown()
t.color("dark blue")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.left(90)
    t.forward(300)
    t.left(90)
t.end_fill()


# Draw Sun
t.penup()
t.goto(-100, 0)
t.setheading(0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.forward(200)
t.left(90)
t.circle(100, 180)
t.end_fill()

# Sun rays
t.color("yellow")
t.pensize(3)
for angle in range(0, 181, 15):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(100)
    t.pendown()
    t.forward(50)


# Draw Birds
bird_positions = [(-275, 150), (-50, 200), (150, 170)]
t.penup()
t.setheading(0)
t.pensize(2)
t.color("black")
for x, y in bird_positions:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(160)
    t.forward(20)
    t.backward(20)
    t.setheading(20)
    t.forward(20)
    t.penup()

t.setheading(0)

# Draw Clouds
def draw_clouds(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    for _ in range(4):
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        t.penup()
        t.forward(30)
        t.pendown()

draw_clouds(-250, 200)
draw_clouds(200, 200)

# Draw Boat

# Hull
t.penup()
t.goto(50, -100)   
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(100)   # width
t.left(90)
t.forward(20)    # height
t.left(90)
t.forward(100)   # width
t.left(90)
t.forward(20)    # height
t.left(90)
t.end_fill()

# Sail (triangle)
t.penup()
t.goto(90, -80)  # bottom-left of sail
t.pendown()
t.color("white")
t.begin_fill()
t.goto(90, 0)    # top of sail
t.goto(130, -80) # bottom-right of sail
t.goto(90, -80)  # back to bottom-left
t.end_fill()

t.hideturtle()
turtle.done()