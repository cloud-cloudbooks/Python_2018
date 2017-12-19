import turtle

def hexagon(size):
    for i in range(6):
        turtle.forward(size)
        turtle.left(60)

hexagon(200)

turtle.done()
