
#Ich zeichne eine Blume

import turtle
t = turtle.Pen()

t.width(8)
t.color('red')

t.begin_fill()
t.circle(45)
t.end_fill()

t.up()
t.goto(75,0)
t.down()

t.begin_fill()
t.circle(45)
t.end_fill()

t.up()
t.forward(45)
t.left(90)
t.forward(105)
t.down()

t.begin_fill()
t.circle(45)
t.end_fill()

t.up()
t.left(90)
t.forward(85)
t.right(90)
t.down()

t.begin_fill()
t.circle(45)
t.end_fill()

#ich zeichne den stiel

t.width(10)
t.color('green')

t.right(180)
t.forward(250)
t.right(180)
t.forward(50)
t.right(45)
t.forward(45)
t.backward(45)
t.left(45)
t.forward(205)

t.color('yellow')
t.left(90)
t.begin_fill()
t.circle(25)
t.end_fill()
