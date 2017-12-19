import turtle

def tilted_square():
  turtle.left(20)     # 각도는 여기서먄 바꿀 수 있음
  for i in range(4):
      turtle.forward(200)
      turtle.left(90)

tilted_square()
tilted_square()
tilted_square()

turtle.done()