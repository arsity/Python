import turtle
import random


def initialization():

    turtle.setup(660, 740)
    turtle.tracer(False)

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
    gl_head.shape('square')
    gl_head.color('red')
    gl_head.goto(0, -40)  # 注意到不同中心

    global motion_status
    motion_status = 'Paused'

    global pointer
    pointer = 'Right'

    global time
    time = 0

    turtle.update()


def placeFruit():
    pass


def statusBar(contact: int, time: float, motion: str):
    status_Turtle = turtle.Turtle(visible=False)
    status_Turtle.penup()
    status_Turtle.goto(0, 250)
    status_Turtle.write("", align='center', font=('Arial', 14, 'normal'))


def go_up():
    global gl_head
    gl_head.sety(gl_head.ycor()+21)
    if gl_head.ycor() > 200:
        gl_head.sety(200)
    turtle.update()


def go_down():
    global gl_head
    gl_head.sety(gl_head.ycor()-21)
    if gl_head.ycor() < -280:
        gl_head.sety(-280)
    turtle.update()


def go_left():
    global gl_head
    gl_head.setx(gl_head.xcor()-21)
    if gl_head.xcor() < -240:
        gl_head.setx(-240)
    turtle.update()


def go_right():
    global gl_head
    gl_head.setx(gl_head.xcor()+21)
    if gl_head.xcor() > 240:
        gl_head.setx(240)
    turtle.update()


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


def direction(direction: str):
    global pointer
    if direction == 'Up':
        pointer = 'Up'
    elif direction == 'Down':
        pointer = 'Down'
    elif direction == 'Left':
        pointer = 'Left'
    elif direction == 'Right':
        pointer = 'Right'


def game():
    global pointer
    print(pointer)
    if pointer == 'Up':
        go_up()
    elif pointer == 'Down':
        go_down()
    elif pointer == 'Left':
        go_left()
    elif pointer == 'Right':
        go_right()
    global time
    time += 0.3
    turtle.update()
    turtle.ontimer(game, 300)


def main():
    initialization()
    turtle.listen()
    turtle.onkey(lambda: direction('Up'), 'Up')
    turtle.onkey(lambda: direction('Down'), 'Down')
    turtle.onkey(lambda: direction('Right'), 'Right')
    turtle.onkey(lambda: direction('Left'), 'Left')
    # turtle.onkey(, 'Space')

    game()
    turtle.mainloop()


main()
