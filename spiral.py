import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("green")
t.width(2)
t.speed(15)

col = ('black', 'yellow', 'cyan')
for i in range (300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)