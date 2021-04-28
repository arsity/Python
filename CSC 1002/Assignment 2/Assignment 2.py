import turtle
import random


def initialization():
    turtle.setup(660, 740)
    frame_Turtle = turtle.Turtle(visible=False)
    turtle.tracer(False)
    frame_Turtle.penup()
    frame_Turtle.goto(-250, 210)
    frame_Turtle.pendown()
    frame_Turtle.goto(-250, -290)
    frame_Turtle.goto(250, -290)
    frame_Turtle.goto(250, 210)
    frame_Turtle.goto(-250, 210)
    frame_Turtle.goto(-250, 290)
    frame_Turtle.goto(250, 290)
    frame_Turtle.goto(250, 210)
    turtle.update()
    turtle.Screen()
    turtle.screensize(500, 500)

    welcomeText_Turtle = turtle.Turtle(visible=False)
    welcomeText_Turtle.penup()
    welcomeText_Turtle.goto(-230, 150)
    welcomeText_Turtle.write('Welcome to the SNAKE GAME!\n',
                             align='left', font=('Arial', 12, 'normal'))


def main():
    initialization()
    snake = turtle.Turtle('square')
    snake.color('red')
    snake.penup()

    snake.forward(100)
    turtle.mainloop()


main()
