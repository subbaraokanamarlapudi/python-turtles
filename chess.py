import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drawSqr():
    for i in range(4):
        t.forward(30)
        t.left(90)
    t.forward(30)
    
if __name__== "__main__" :
    s.setup(600,600)
    t.speed(100)
    for i in range(8):
        t.up()
        t.setpos(0, 30*i)
        t.down()

        for j in range(8):
            if (i + j)% 2 == 0:
                col = 'black'
            else:
                col = 'white'
            t.fillcolor(col)
            t.begin_fill()
            drawSqr()
            t.end_fill()
        t.hideturtle()
