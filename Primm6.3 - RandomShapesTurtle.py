#Name:
#Purpose: Drawing shapes in random locations with Turtle
#Date:

import random
import turtle

t = turtle.Pen()
#Set the background colour
turtle.bgcolor("black")
t.pencolor("red")

# Generate a random (x,y) location on the screen and move the turtle there
x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
t.penup()
t.setpos(x,y)
t.pendown()

#draw a squared spiral with 10 sides
for m in range(10):
        t.forward(m*2)
        t.left(91)

"""
1. Change the spiral to be a random number of sides between 10 and 50
2. Make the turtle colour be a random choice from the following list
"red", "yellow", "blue", "green", "orange", "purple","white", "gray"
3. Change the code to have the program repeat the spiral 4 different times, 
with each spiral having a randomly chosen colour, random number of sides and a random starting point.
4. For each new spiral have the program randomly choose to turn one of the following angles.
61, 73, 91, 121
"""