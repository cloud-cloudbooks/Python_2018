import turtle

pen = turtle.Turtle()

v_distance = 100
v_angle    = 90


for i in range(4):
    pen.right(v_angle)
    pen.forward(v_distance)

for i in range(4):
    for j in range(3):
        pen.forward(v_distance)
        if j<2:
            pen.right(v_angle)
        else  :
            pen.left(v_angle)

    # pen.forward(50)
    # pen.right(90)
    # pen.forward(50)
    # pen.right(90)
    # pen.forward(50)
    # pen.left(90)


turtle.done()