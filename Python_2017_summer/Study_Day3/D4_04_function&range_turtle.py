# function과 range 이용해 선을 반복해서 그려보자
# 변수 angle 값을 89에서 점점 낮은 숫자로 해보자. (89, 79, 69, 59...)

import turtle as t

angle = 89
t.bgcolor("black")
t.color("yellow")
t.speed(9)
for x in range(500):
    t.forward(x)
    t.left(angle)
t.mainloop()



