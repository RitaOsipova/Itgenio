# Ampel und Blume
import turtle
t = turtle.Pen()

t.width(8)

t.goto(0,220)
t.goto(124,220)
t.goto(124,0)
t.goto(0,0)
t.up()
t.goto(62,0)
t.down()
t.right(90)
t.forward(100)
t.right(90)
t.forward(62)
t.backward(124)
t.up()
t.goto(90,0)
t.down()
t.right(90)
t.up()
t.forward(40)
t.down()
#ich male den gunen kreis
t.color('green')
t.begin_fill()
t.circle(28)
t.end_fill()
#ich male den gelben kreis
t.up()
t.forward(70)
t.down()
t.color('yellow')
t.begin_fill()
t.circle(28)
t.end_fill()
#ich male den roten kreis
t.up()
t.forward(70)
t.down()
t.color('red')
t.begin_fill()
t.circle(28)
t.end_fill()
