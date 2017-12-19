# 변수와 for / range 이용해서 다각형 그려보기
# (5~20 숫자 넣어보기. 아주 큰 값 넣으면 어떻게 될까?)

import turtle as t

n = 5
t.color("red")
t.begin_fill()

for x in range(n) :
    t.forward(50)
    t.left(360/n)
t.end_fill()
