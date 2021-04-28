import turtle
import random


def initialization():

    turtle.setup(660, 740)
    turtle.tracer(False, 300)

    frame_turtle = turtle.Turtle(visible=False)
    frame_turtle.penup()
    frame_turtle.goto(-250, 210)
    frame_turtle.pendown()

    for _ in range(4):
        frame_turtle.forward(500)
        frame_turtle.right(90)

    for _ in range(2):
        frame_turtle.forward(500)
        frame_turtle.left(90)
        frame_turtle.forward(80)
        frame_turtle.left(90)

    welcomeText_turtle = turtle.Turtle(visible=False)
    welcomeText_turtle.penup()
    welcomeText_turtle.goto(-230, 150)
    welcomeText_turtle.write('Welcome to the SNAKE GAME!\n',
                             align='left', font=('Arial', 12, 'normal'))

    global gl_head
    gl_head = turtle.Turtle()
    gl_head.penup()
    gl_head.color('red')
    gl_head.goto(0, -40)  # 注意到不同中心

    global motion_status
    motion_status='Paused'


def placeFruit():
    pass


def statusBar(contact: int, time: float, motion: str):
    status_Turtle = turtle.Turtle(visible=False)
    status_Turtle.penup()
    status_Turtle.goto(0, 250)
    status_Turtle.write("", align='center', font=('Arial', 14, 'normal'))


def storeMotion(motion: str) -> str:
    pass


def move(motion: str):
    global gl_head
    x = y = 0
    if motion == 'Up':
        y = 1
    elif motion == 'Down':
        y = -1
    elif motion == 'Left':
        x = -1
    elif motion == 'Right':
        x = 1
    gl_head.goto(gl_head.xcor()+x, gl_head.ycor()+y)

    if gl_head.xcor() < -250:
        gl_head.setx(-250)
    elif gl_head.xcor() > 250:
        gl_head.setx(250)
    if gl_head.ycor() < -290:
        gl_head.sety(-290)
    elif gl_head.ycor() > 210:
        gl_head.sety(210)


def draw(locationList: list) -> list:  # 注意改回坐标
    global gl_head
    stampId_list = []
    gl_head.color('blue', 'black')
    for location in locationList:
        gl_head.goto(location)
        stamp_Id = gl_head.stamp()
        stampId_list.append(stamp_Id)
    gl_head.color('red')
    return stampId_list


def game():
    global motion_status
    motion_status='Paused'
    


def main():
    initialization()
    turtle.ontimer(game(), 300)
    turtle.mainloop()


main()
