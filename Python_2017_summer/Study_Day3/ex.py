#section_056.py

import turtle

t = turtle.Pen()
t.shape("turtle")

color = int(input('색을 선택하세요(1:파랑, 2:빨강, 3:노랑): '))

if color == 1 :
    t.color("blue")
elif color == 2 :
    t.color("red")
elif color == 3 :
    t.color("yellow")
else :
    t.color("black")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

turtle.done()
