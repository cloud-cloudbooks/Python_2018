import turtle

ninja = turtle.Turtle()
# turtle 나라에서 온  Turtle() 법을 따르는 ninja

ninja.speed(10)

for i in range(90):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(4)





turtle.done()