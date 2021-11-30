#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:31:24 2021

@author: jeremybill
"""

import turtle
#function to draw the house
def house(outline,fill,size):
   #sets the position for the house and color
    turtle.penup()
    turtle.setposition(-50,0)
    turtle.color(outline,fill)
    turtle.pendown()
    #begins the fill
    turtle.begin_fill()
    #for loop to draw the square that is the house
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    #ends the fill
    turtle.end_fill()
#function to draw the rooof. Note: It does not move the turtle since it is already in position
def roof(outline,fill,size):
    turtle.color(outline,fill)
    turtle.begin_fill()
    #for loop to draw the triangle that serves as the roof of the house
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
#function to draw a star
def star(size,outline,fill,x,y):
    turtle.penup()
    turtle.color(outline,fill)
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.begin_fill()
    #draws 5 stars
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
#sets some variables and bg color
turtle.bgcolor("gray")
startx=-250
starty=200
turtle.hideturtle()
#draws 5 stars
for i in range(5):
    star(50,"yellow","yellow",startx,starty)
    startx=startx+100
#draws the moon
turtle.penup()
turtle.setposition(225,225)
turtle.color("white","white")
turtle.pendown()
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
#calls house and roof while setting their colors and sizes
house("blue","blue",100)
roof("red","red",100)
#draws a window on the house
turtle.penup()
turtle.setposition(-40,-50)
turtle.color("green","green")
turtle.pendown()
turtle.begin_fill()
#goes left to start the window
turtle.lt(90)
turtle.forward(20)
#then for 3 times it will go right then forward
for i in range(3):
    turtle.rt(90)
    turtle.forward(20)
turtle.end_fill()
#draws a door on the house
turtle.penup()
turtle.setposition(-15,-100)
turtle.color("brown","brown")
turtle.pendown()
turtle.begin_fill()
#did not loop this since you have to go forward various lengths 
turtle.rt(90)
turtle.forward(30)
turtle.rt(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()
#exits the program on click 
turtle.exitonclick()

    