#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import time
import random

# Rectangle function using dimensions from Wikipedia.
def draw_rectangle(length, height, color):
    turtle.up()
    x = -(0.75*height)
    y = (0.75*height)
    C = height*(7/13)
    D = length*(2/5)
    # stripe_width - 0.3 to account for black outline
    L = stripe_width = float(round(height/13,1))-0.3

    ## Draw rectangle first.
    turtle.color(get_color(color))
    turtle.begin_fill()
    turtle.setpos(x-4,y+4)
    turtle.down()
    turtle.forward(length+4)
    turtle.right(90)
    turtle.forward(height+4)
    turtle.right(90)
    turtle.forward(length+4)
    turtle.right(90)
    turtle.forward(height+4)
    turtle.end_fill()

    ## Then draw the stripes.
    x1 = -(0.75*height)
    y1 = (0.75*height)-L
    for z in range(13):
        turtle.up()
        turtle.speed(100)
        turtle.setpos(x1,y1)
        turtle.setheading(90)
        turtle.down()
        # Use length - 3 to account for black outline.
        if z%2 == 0:
            turtle.color(get_color('red'))
            turtle.begin_fill()
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length-3)
            turtle.right(90)
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length-3)
            turtle.end_fill()
            y1 -= L
        else:
            turtle.color(get_color('white'))
            turtle.begin_fill()
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length-3)
            turtle.right(90)
            turtle.forward(L)
            turtle.right(90)
            turtle.forward(length-3)
            turtle.end_fill()
            y1 -= L
    
        
    ## Finally, draw the blue stars rectangle on top of the stripes.
    color = 'blue'
    x2 = -(0.75*height)+D
    # Use +0.5 to account for black outline.
    y2 = (0.75*height)+0.5-C
    turtle.up()
    turtle.setpos(x2,y2)
    turtle.down()
    turtle.color(get_color(color))
    turtle.begin_fill()
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.right(90)
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.end_fill()
    turtle.up()

    turtle.bye
    draw_star(height, 'white')

# Draw the stars.
# Create star rows.
def draw_star(size, color):
    turtle.color(get_color('white'))
    for z in range(100):
        if z < 7:
            row = size/1.43
            draw_starrows(size,row)
        if z < 14:
            row = row - size/20
            draw_starrows2(size,row)
        if z < 21:
            row = row - size/20
            draw_starrows(size,row)
        if z < 28:
            row = row - size/20
            draw_starrows2(size,row)
        if z < 35:
            row = row - size/20
            draw_starrows(size,row)
        if z < 42:
            row = row - size/20
            draw_starrows2(size,row)
        if z < 49:
            row = row - size/20
            draw_starrows(size,row)
        if z < 56:
            row = row - size/20
            draw_starrows2(size,row)
        if z < 63:
            row = row - size/20
            draw_starrows(size,row)
            ## This gets the turtle pen out of the way at the very end.
            turtle.up()
            # -(size/1.111) was -180 and (size/2) was 100
            turtle.setpos(-(size/1.111),(size/2))
        break
# Code for where the star rows start 
# Code for the 5 rows of 6 stars
def draw_starrows(size,row):
    x = -(size/20)-(0.75*size)
    y = 0.75*size
    for z in range(6):
        x += (size/8.696)
        turtle.up()
        turtle.color(1,1,1)
        turtle.speed(100)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.end_fill()
# Code for the 4 rows of 5 stars
def draw_starrows2(size,row): 
    x = -0.75*size
    y = 0.75*size
    for z in range(5):
        x += (size/8.696)
        turtle.up()
        turtle.color(1,1,1)
        turtle.speed(100)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.forward(size/32.5)
        turtle.left(144)
        turtle.end_fill()
    turtle.bye

# Turn colors with type string into colors that turtle can read.
def get_color(color):
    if color == 'red':
        return 1,0,0
    if color == 'white':
        return 1,1,1
    if color == 'blue':
        return 0,0,1
    # This will return black in our program.
    else:
        return 0,0,0

# Draw flag using dimensions given in Wikipedia page linked.
def draw_flag(height):
    length = height*1.9
    C = height*(7/13)
    D = length*(2/5)
    stripe_width = height/13
    diameter_star = stripe_width*(4/5)
    draw_rectangle(height*1.9, height, 'black')

# Use main function and set the base height A
def main():
    A = 300
    draw_flag(float(A)) 
  
  
# Using the special variable __name__
if __name__=="__main__":
    main()
    
# Tell turtle to stop running.
turtle.done()


# In[ ]:




