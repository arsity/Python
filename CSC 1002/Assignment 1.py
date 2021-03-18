import copy  # for deep copy
import string  # for ascii letter list


def integer_test(n):  # test an integer from 3 to 10
    number_List = []
    for i in range(3, 11):
        number_List.append(str(i))
    if n in number_List:
        return True
    return False


def bind_key():  # bind custom key
    # printing words
    VALID_LIST = list(string.ascii_letters)
    WORD_LIST = ['Enter the key that you can let the number under the space go up: ', 'Enter the key that you can let the number above the space go down: ',
                 'Enter the key that you can let the number on the left side of the space go right: ', 'Enter the key that you can let the number on the right side of the space go left: ']
    bind_Key_List = []
    for i in range(0, 4):
        while True:
            key = input(WORD_LIST[i])
            if key in VALID_LIST:  # test one letter
                if key not in bind_Key_List:  # test used before
                    bind_Key_List.append(key)
                    break
                print(
                    "This key has been bound to another action! Please enter another letter!")
            else:
                print("Invalid binding key! Please enter a letter!")
    return bind_Key_List


def generating(n, total_List):  # generate the matrix in order
    for row in range(0, n):  # generate the full matrix
        list_Temp = list(range(row*n+1, row*n+n+1))
        total_List.append(list_Temp)
    total_List[n-1][n-1] = " "  # replace the last one as ' '
    global gl_Place
    gl_Place = [n-1, n-1]  # state the location of the space
    return total_List


# translate custom key to standard order
def translate(operaion_List, bind_Key_List, gl_Place, n):
    translation = None
    print('Enter one of', end=' ')  # print the key can be chosen
    if gl_Place[0] != n-1:
        print('up-', bind_Key_List[0], sep='', end=' ')
    if gl_Place[0] != 0:
        print('down-', bind_Key_List[1], sep='', end=' ')
    if gl_Place[1] != 0:
        print('left-', bind_Key_List[2], sep='', end=' ')
    if gl_Place[1] != n-1:
        print('right-', bind_Key_List[3], sep='', end='')
    op = input(': ')
    if op == bind_Key_List[0]:  # translate the custom key
        translation = 'up'
    elif op == bind_Key_List[1]:
        translation = 'down'
    elif op == bind_Key_List[2]:
        translation = 'left'
    elif op == bind_Key_List[3]:
        translation = 'right'
    return translation


def operation(op, l):  # move space operation
    global n
    global gl_Place
    y = 0  # y-axis movement in coordinate
    x = 0  # x-axis movement in coordinate
    if op == 'up' and gl_Place[0] != n-1:
        y = 1
    elif op == 'down' and gl_Place[0] != 0:
        y = -1
    elif op == 'left' and gl_Place[1] != 0:
        x = -1
    elif op == 'right' and gl_Place[1] != n-1:
        x = 1
    l[gl_Place[0]][gl_Place[1]] = l[gl_Place[0]+y][gl_Place[1]+x]
    l[gl_Place[0]+y][gl_Place[1]+x] = ' '  # change the position
    gl_Place[0] = gl_Place[0]+y
    gl_Place[1] = gl_Place[1]+x  # change the coordinate position of the ' '
    return l


def mess(a, operaion_List):  # make a random table at start
    import random
    for i in range(0, 10000):
        op = random.choice(operaion_List)
        a = operation(op, a)
    return a


def display(a):  # display the table
    for row in a:
        for column in row:
            print("%+3s" % (column), end=" ")  # to display on certain position
        print("\n", end="")


while True:
    # determine the size of the table
    while True:
        n = input("Enter an integer from 3 to 10 to determine the size: ")
        if integer_test(n) == True:
            n = int(n)
            break
        print("Please enter an integer from 3 to 10!")

    # initialization
    bind_Key_List = bind_key()
    operaion_List = ['up', 'down', 'left', 'right']
    count = 0  # define the count to calculate steps
    gl_Place = [0, 0]  # initialize location of the space
    gl_Total_List = []  # initialize the matrix
    gl_Total_List = generating(n, gl_Total_List)
    initial_List = copy.deepcopy(gl_Total_List)  # save the original matrix
    gl_Total_List = mess(gl_Total_List, operaion_List)
    display(gl_Total_List)

    while True:
        # to judge if invalid operation in followings
        list_For_Judge = copy.deepcopy(gl_Total_List)
        gl_Total_List = operation(translate(operaion_List, bind_Key_List, gl_Place, n),
                                  gl_Total_List)  # change the matrix
        display(gl_Total_List)
        count += 1
        if list_For_Judge == gl_Total_List:
            count += -1  # if invalid, cancel the counting step
            print("Invalid Operation!")
        elif gl_Total_List == initial_List:  # to judge if finish
            print("Congratulations!", "You finish in", count, "steps.")
            break

    # restart module
    while True:
        restart_Sign = input(
            "Do you want to start a new game? (y-Yes, n-No): ")
        if restart_Sign in ['Y', 'y', 'N', 'n']:
            break
    if restart_Sign in ['Y', 'y']:
        continue
    break
