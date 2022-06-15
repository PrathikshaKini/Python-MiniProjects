# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:00:21 2022

@author: HP
"""
import turtle

turtle.bgcolor("lightpink")
turtle.pensize(1.5)
turtle.speed(0.5)
color=["red","blue","green","orange"]

for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()