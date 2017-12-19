import turtle

def draw_shape(sides, length):
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)
        # turtle.right(360 / sides)

draw_shape(3, 200)
draw_shape(4, 200)
draw_shape(5, 200)
draw_shape(8, 100)

turtle.done()