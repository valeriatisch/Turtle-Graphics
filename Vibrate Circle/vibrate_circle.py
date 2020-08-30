import turtle

c = turtle.Turtle()
turtle.bgcolor('black')
c.speed(0)
c.color('lime green')
c.hideturtle()
c.penup()
c.goto(0, 200)
c.pendown()

j = 0

for i in range(210):
    c.forward(j)
    c.right(i)
    j += 3

turtle.mainloop()
