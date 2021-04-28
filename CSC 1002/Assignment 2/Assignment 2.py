import turtle
import random


def initialization():

    turtle.setup(660, 740)
    turtle.tracer(False, 300)
    frame_Turtle = turtle.Turtle(visible=False)
    frame_Turtle.penup()
    frame_Turtle.goto(-250, 210)
    frame_Turtle.pendown()

    for _ in range(4):
        frame_Turtle.forward(500)
        frame_Turtle.right(90)

    for _ in range(2):
        frame_Turtle.forward(500)
        frame_Turtle.left(90)
        frame_Turtle.forward(80)
        frame_Turtle.left(90)
    turtle.update()

    welcomeText_Turtle = turtle.Turtle(visible=False)
    welcomeText_Turtle.penup()
    welcomeText_Turtle.goto(-230, 150)
    welcomeText_Turtle.write('Welcome to the SNAKE GAME!\n',
                             align='left', font=('Arial', 12, 'normal'))


def placeFruit():
    pass


def draw(head: turtle, locationList: list) -> list:
    stampId_List = []
    head.color('blue', 'black')
    for location in locationList:
        head.goto(location)
        stamp_Id = head.stamp()
        stampId_List.append(stamp_Id)
    head.color('red')
    return stampId_List


def statusBar(contact: int, time: float, motion: str):
    status_Turtle = turtle.Turtle(visible=False)
    status_Turtle.penup()
    status_Turtle.goto(0, 250)
    status_Turtle.write("", align='center', font=('Arial', 14, 'normal'))


def move(motion: str):
    

def game():
    pass


def main():
    initialization()
    turtle.ontimer(game(), 300)
    turtle.mainloop()


main()
