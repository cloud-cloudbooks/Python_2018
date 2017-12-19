# while 문으로 거북이를 그려보자

import turtle as t

t.shape("turtle")
count = 0

while count < 4:
    t.forward(100)
    t.left(90)

    count = count + 1

