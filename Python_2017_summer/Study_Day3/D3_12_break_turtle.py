# break는 반복을 중지시킨다
import turtle

t = turtle.Pen()
t.shape("turtle")

for item in range(30):
    if item % 2:   #나머지는 0, 1인데 0은 False를 나타냄
        t.pendown()
    else:
        t.penup()
    if item == 10:
        break
    t.forward(10)
turtle.done()

