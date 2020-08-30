import turtle

c = turtle.Turtle()
turtle.bgcolor('black')
c.pensize(2)
c.speed(0)

colours = ["sky blue", "medium spring green", "gold", "crimson", "blue", "aquamarine", "plum"]

for i in range(5):
    for col in colours:
        c.color(col)
        c.left(12)
        c.forward(200)
        c.left(90)
        c.forward(200)
        c.left(90)
        c.forward(200)
        c.left(90)
        c.forward(200)
        c.left(90)

turtle.mainloop()
