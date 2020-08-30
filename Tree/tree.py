import turtle

MINIMUM_BRANCH_LENGTH = 5


# recursive function
# t: turtle instance
# branch_length: current branch len in px
# shorten_by: by how many px the sub branches will be shorten
# angle: angles from which the sub branches emerge
def build_tree(t, branch_length, shorten_by, angle):
    # base case: if branch len is lower than minimum
    if branch_length > MINIMUM_BRANCH_LENGTH:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)
        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_length)


# object moving aroung the canvas and drawing the tree
tree = turtle.Turtle()
# background color
turtle.bgcolor('black')
# speed up
tree.speed(0)
# make the turtle invisible
tree.hideturtle()
# make it face upwards
tree.setheading(90)
# colors https://trinket.io/docs/colors
tree.color('aquamarine')
# bigger lines
tree.pensize(2)

build_tree(tree, 50, 5, 30)
turtle.getcanvas().postscript(file="Tree/tree.eps")
