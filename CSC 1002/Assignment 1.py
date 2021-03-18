import copy  # for deep copy
import string  # for ascii letter list


def integer_test(n):  # test an integer from 3 to 10
    k = []
    for i in range(3, 11):
        k.append(str(i))
    if n in k:
        return True
    return False


def key_valid_test(s):  # test a letter
    valid_List = list(string.ascii_letters)
    if s in valid_List:
        return True
    return False


def bind_key():  # bind custom key
    # printing words
    word_list = ['Enter the key that you can let the number under the space go up: ', 'Enter the key that you can let the number above the space go down: ',
                 'Enter the key that you can let the number on the left side of the space go right: ', 'Enter the key that you can let the number on the right side of the space go left: ']
    bind_Key_List = []
    for i in range(0, 4):
        while True:
            key = input(word_list[i])
            if key_valid_test(key) == True:  # test one letter
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
        list_temp = list(range(row*n+1, row*n+n+1))
        total_List.append(list_temp)
    total_List[n-1][n-1] = " "  # replace the last one as ' '
    global place
    place = [n-1, n-1]  # state the location of the space
    return total_List


def translate(operaion_List, bind_Key_List, place, n):  # translate custom key to standard order
    translation = None
    print('Enter one of', end=' ')  # print the key can be chosen
    if place[0] != n-1:
        print(bind_Key_List[0], end=' ')
    if place[0] != 0:
        print(bind_Key_List[1], end=' ')
    if place[1] != 0:
        print(bind_Key_List[2], end=' ')
    if place[1] != n-1:
        print(bind_Key_List[3], end='')
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
    global place
    a = 0  # y-axis movement in coordinate
    b = 0  # x-axis movement in coordinate
    if op == 'up' and place[0] != n-1:
        a = 1
    elif op == 'down' and place[0] != 0:
        a = -1
    elif op == 'left' and place[1] != 0:
        b = -1
    elif op == 'right' and place[1] != n-1:
        b = 1
    l[place[0]][place[1]] = l[place[0]+a][place[1]+b]
    l[place[0]+a][place[1]+b] = ' '  # change the position
    place[0] = place[0]+a
    place[1] = place[1]+b  # change the coordinate position of the ' '
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
    place = [0, 0]  # initialize location of the space
    total_List = []  # initialize the matrix
    total_List = generating(n, total_List)
    initial_List = copy.deepcopy(total_List)  # save the original matrix
    total_List = mess(total_List, operaion_List)
    display(total_List)

    while True:
        # to judge if invalid operation in followings
        list_For_Judge = copy.deepcopy(total_List)
        total_List = operation(translate(operaion_List, bind_Key_List, place, n),
                               total_List)  # change the matrix
        display(total_List)
        count += 1
        if list_For_Judge == total_List:
            count += -1  # if invalid, cancel the counting step
            print("Invalid Operation!")
        elif total_List == initial_List:  # to judge if finish
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
