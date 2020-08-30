import turtle


# recursive function
# t: turtle instance
# iterations:
# length: len of each side in current snowflake
# shortening_factor: factor by which the side len is divided when creating a new sub snowflake
# angle: from which the new side emerge
def build_curve(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations -= 1
        length /= shortening_factor

        build_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        build_curve(t, iterations, length, shortening_factor, angle)
        t.right(angle * 2)
        build_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        build_curve(t, iterations, length, shortening_factor, angle)


s = turtle.Turtle()
s.speed(0)
s.hideturtle()
s.color('light blue')
turtle.bgcolor('black')
turtle.penup()
for i in range(3):
    build_curve(s, 4, 200, 3, 60)
    s.right(120)

turtle.getcanvas().postscript(file="koch_snowflake.eps")

turtle.mainloop()
