import turtle
from math import sin
from turtle import done

t=turtle.Turtle(shape='turtle')
screen=turtle.Screen()
t.speed(0)

### Pythagoras tree ###

# === Square drawing function ===
def square_left(side):

    for i in range(4):
        t.forward(side)
        t.left(90)

def square_right(side):

    for i in range(4):
        t.forward(side)
        t.right(90)

# === end of function ===

def branch_left():
    side=100
    square_left(side)
    side=side*(2**(1/2))/2
    t.right(45)
    for i in range(10):
        square_right(side)
        t.right(90)
        t.forward(side)
        t.left(45)
        side=side*(2**(1/2))/2

def branch_right():
    side=100
    square_left(side)
    t.forward(side)
    side=side*(2**(1/2))/2
    t.right(45)
    for i in range(10):
        square_right(side)
        t.right(90)
        t.forward(side)
        t.left(45)
        side=side*(2**(1/2))/2

while True:
    branch_left()
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.left(135)
    branch_right()

done()