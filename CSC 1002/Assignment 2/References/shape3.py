from turtle import Turtle
import math

g_pen = None

def square(length):
    polygon(4, length)

def polygon(side, length, span=360):
    angle = span/side
    for i in range(side):
        g_pen.forward(length)
        g_pen.left(angle)

def circle(r):
    arc(r, 360)

def arc(r, span):
    cir = 2 * math.pi * r * span/360
    side = int(cir/3)
    length = cir/side
    polygon(side, length, span)

if __name__ == "__main__":
    g_pen = Turtle()
    square(100)
    polygon(6,100)
    circle(100)
    g_pen.color("red")
    arc(100,180)
    g_pen.screen.mainloop()
