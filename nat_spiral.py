import turtle
from math import sin

t=turtle.Turtle(shape='turtle')
t.speed(0)

s=600
a=10
for n in range (1000):
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.setheading(0)
    t.left(a)
    s-=4
    a+=2

    
    


