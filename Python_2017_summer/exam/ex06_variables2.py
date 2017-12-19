# 원하는 다각형을 그려보자

import turtle

polygon = turtle.Turtle()

var1 = input('면의 수는?')
var2 = input('면의 길이?')

num_sides = int(var1)
side_length = int(var2)
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()