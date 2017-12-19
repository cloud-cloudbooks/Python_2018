# function을 이용해 원그리기

import turtle as t

n = 30
t.bgcolor("black")
t.color("red")
t.speed(0)

for x in range(n):
    t.circle(100)
    t.left(360/n)

t.done()