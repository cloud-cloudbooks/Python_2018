import turtle

def tilted_line_without_moving(length, angle):
    turtle.left(angle)
    turtle.forward(length)
    turtle.backward(length)

tilted_line_without_moving(60, 200)

turtle.done()
