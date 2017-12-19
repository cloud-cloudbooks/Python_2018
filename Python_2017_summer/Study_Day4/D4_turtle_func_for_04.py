import turtle

# bonus: you could have a separate function for drawing a square,
# which might be useful later:

def square():
  for _ in range(4):
      turtle.forward(200)
      turtle.left(90)

def tilted_square():
  turtle.left(20)
  square()

for _ in range(3):
    tilted_square()

turtle.done()