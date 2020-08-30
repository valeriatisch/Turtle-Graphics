import turtle

s = turtle.Turtle()
s.penup()
turtle.bgcolor('dim grey')

s.fillcolor('orange')
s.begin_fill()
for i in range(4):
    s.forward(100)
    s.right(90)
s.end_fill()

s.fillcolor('dark orange')
s.begin_fill()
s.left(90 + 45)
s.forward(50)

s.left(90 + 45)
s.forward(100)

s.left(45)
s.forward(50)

s.end_fill()

s.right(45)
s.backward(100)

s.fillcolor('sandy brown')
s.begin_fill()
s.right(90 + 45)
s.forward(50)

s.right(45 + 90)
s.forward(100)
s.right(45)
s.forward(50)
s.hideturtle()
s.end_fill()

turtle.mainloop()
