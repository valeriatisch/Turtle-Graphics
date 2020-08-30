import turtle

c = turtle.Turtle()
turtle.bgcolor('black')
c.pensize(2)
c.hideturtle()
c.speed(0)

colours = ["misty rose", "pink", "light pink", "pale violet red", "violet", "plum", "seashell"]

for i in range(6):
    for col in colours:
        c.color(col)
        c.circle(100)
        c.left(10)

turtle.getcanvas().postscript(file="circle_spirograph.eps")

turtle.mainloop()
