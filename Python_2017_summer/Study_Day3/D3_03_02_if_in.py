import turtle as t

t.shape("turtle")

reptilia = ['turtle', 'crocodile', 'iguana', 'chameleon']

if 'turtle' in reptilia:
    t.color('red')
    t.forward(100)

if 'lion' not in reptilia:
    t.color('yellow')
    t.forward(100)

t.done()