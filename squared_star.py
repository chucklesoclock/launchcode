"""
Creates a star using a four-square figure.
Hard-coded to draw the four-square 5 times, equally rotated along 180 degrees. 
Only certain numbers guarantee non-reptition of four-square being drawn. 
TODO: Math to determine which could reduce the number of figures necessary. 
"""

import turtle as t

def line(length, turt):
    turt.forward(length / 2)
    turt.forward(-length)
    turt.forward(length / 2)
    
def cross_and_two_sides(spread, turt):
    line(spread, turt)
    turt.left(90)
    turt.forward(spread/2)
    turt.right(90)
    line(spread, turt)
    turt.right(90)
    turt.forward(spread)
    turt.left(90)
    line(spread, turt)
    
def other_two_sides(length, turt):
    turt.forward(length/2)
    turt.left(90)
    turt.forward(length)
    turt.left(90)
    turt.forward(length)
    turt.left(90)
    turt.forward(length)
    turt.left(90)
    turt.penup()
    turt.goto(0,0)
    turt.pendown()

def four_sq(angle, turt, length=200):
    turt.left(angle)
    cross_and_two_sides(length, turt)
    other_two_sides(length, turt)
    turt.home()
    
def starred_4sqs(num, turt):
    for angle in range(0, 180, int(180/num)):
        four_sq(angle, turt)
        
gio = t.Turtle()
gio.speed(10)
starred_4sqs(5, gio)
gio.hideturtle()
