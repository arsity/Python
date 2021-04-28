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
    gl_head = turtle.Turtle(visible=True)
    gl_head.penup()
    gl_head.shape('square')
    gl_head.color('red')
    gl_head.goto(0, -40)  # 注意到不同中心

    global gl_monster
    gl_monster = turtle.Turtle()
    gl_monster.penup()
    gl_monster.shape('square')
    gl_monster.color('purple')

    x1 = random.choice((0, 1))
    y1 = random.choice((0, 1))
    x = 20*random.randint(5, 10)
    if x1 == 1:
        x = -x
    if y1 == 0:
        y = 20*random.randint(3, 8)
    else:
        y = 20*random.randint((-12, -7))

    gl_monster.goto(x, y)

    global motion_status
    motion_status = 'Paused'

    global pointer
    pointer = 'Right'

    global collision
    collision = 0

    global time
    time = 0

    global locationList
    locationList = [(0, -40)]

    global flag
    flag = False

    turtle.update()


def Fruit():
    f1=turtle.Turtle(visible=False)
    f2=turtle.Turtle(visible=False)
    f3=turtle.Turtle(visible=False)
    f4=turtle.Turtle(visible=False)
    f5=turtle.Turtle(visible=False)
    f6=turtle.Turtle(visible=False)
    f7=turtle.Turtle(visible=False)
    f8=turtle.Turtle(visible=False)
    f9=turtle.Turtle(visible=False)

    f1.write('1',align='center',font=('Arial',12,'normal'))
    f2.write('2',align='center',font=('Arial',12,'normal'))
    f3.write('3',align='center',font=('Arial',12,'normal'))
    f4.write('4',align='center',font=('Arial',12,'normal'))
    f5.write('5',align='center',font=('Arial',12,'normal'))
    f6.write('6',align='center',font=('Arial',12,'normal'))
    f7.write('7',align='center',font=('Arial',12,'normal'))
    f8.write('8',align='center',font=('Arial',12,'normal'))
    f9.write('9',align='center',font=('Arial',12,'normal'))




def statusBar(contact: int, time: float, motion: str):
    status_Turtle = turtle.Turtle(visible=False)
    status_Turtle.penup()
    status_Turtle.goto(0, 250)
    status_Turtle.write("", align='center', font=('Arial', 14, 'normal'))


def catch():
    global gl_head
    global gl_monster
    X_Distance = gl_head.xcor()-gl_monster.xcor()
    Y_Distance = gl_head.ycor()-gl_monster.ycor()
    if abs(X_Distance) >= abs(Y_Distance):
        if X_Distance > 0:
            gl_monster.setx(gl_monster.xcor()+20)
        else:
            gl_monster.setx(gl_monster.xcor()-20)
    else:
        if Y_Distance > 0:
            gl_monster.sety(gl_monster.ycor()+20)
        else:
            gl_monster.sety(gl_monster.ycor()-20)

    global collision
    global gl_bodyLocation
    for (x, y) in gl_bodyLocation:
        if abs(gl_monster.xcor()-x) < 16 and abs(gl_monster.ycor()-y) < 16:
            collision += 1
            break
    if abs(gl_monster.xcor()-gl_head.xcor()) < 8 and abs(gl_monster.ycor()-gl_head.ycor()) < 8:
        global flag
        flag = True

    if flag:
        pass
    else:
        turtle.ontimer(catch, random.randint(280, 400))


def go_up():
    global gl_head
    gl_head.sety(gl_head.ycor()+20)
    if gl_head.ycor() > 200:
        gl_head.sety(200)
        return True


def go_down():
    global gl_head
    gl_head.sety(gl_head.ycor()-20)
    if gl_head.ycor() < -280:
        gl_head.sety(-280)
        return True


def go_left():
    global gl_head
    gl_head.setx(gl_head.xcor()-20)
    if gl_head.xcor() < -240:
        gl_head.setx(-240)
        return True


def go_right():
    global gl_head
    gl_head.setx(gl_head.xcor()+20)
    if gl_head.xcor() > 240:
        gl_head.setx(240)
        return True


def draw(locationList: list, snakeLength: int) -> list:  # 注意改回坐标
    global gl_head
    save = locationList[0]
    gl_head.color('black', 'green')
    gl_head.clearstamps()
    for location in locationList[0:snakeLength]:
        gl_head.goto(location)
        gl_head.stamp()
    gl_head.color('black', 'red')
    gl_head.goto(save)
    global gl_bodyLocation
    gl_bodyLocation = locationList[0:snakeLength]


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
    global locationList
    global gl_head
    global pointer
    if pointer == 'Up':
        k = go_up()
    elif pointer == 'Down':
        k = go_down()
    elif pointer == 'Left':
        k = go_left()
    elif pointer == 'Right':
        k = go_right()

    if k:
        pass
    else:
        locationList.insert(0, gl_head.pos())

    draw(locationList, 2)
    # print(pointer)
    # print(locationList)

    global time
    time += 0.3

    global flag
    if flag:
        turtle.update()
        pass
    else:
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
    catch()
    turtle.mainloop()


main()
