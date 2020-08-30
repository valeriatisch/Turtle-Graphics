import time
import turtle
from random import randint

# window setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("sea green")
turtle.color("white")
# turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write('Turtle Race', font=('Comic Sans MS', 25, 'bold'))
turtle.penup()

# finish line
stamp_size = 20
square_size = 15
finish_line = 250

turtle.color('black')
turtle.shape('square')
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()
    turtle.setpos(finish_line + 15, (135 - (i * square_size * 2)))
    turtle.stamp()

turtle.color('white')
for i in range(10):
    turtle.setpos(finish_line, (135 - (i * square_size * 2)))
    turtle.stamp()
    turtle.setpos(finish_line + 15, (150 - (i * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# turtles
colors = ['gold', 'light pink', 'light blue', 'lavender']
turtles = []
h = 0
for c in colors:
    t = turtle.Turtle()
    t.speed(0)
    t.shape('turtle')
    t.color(c)
    t.penup()
    t.goto(-250, 100 - h)
    h += 50
    t.pendown()
    turtles.append(t)

time.sleep(1)

# move the turtles
winner = None
while not winner:
    for t in turtles:
        t.forward(randint(1, 10))
        t.left(randint(-4, 4))
        if t.xcor() >= finish_line:
            winner = t
            break
        else:
            continue

turtle.setpos(0, 0)
turtle.color('brown')
turtle.write("The {} turtle won the race!".format(winner.pencolor()),
             font=('Comic Sans MS', 30, 'bold'), align='center')
turtle.penup()

turtle.mainloop()
