def generating(n):  # generating the initial table in order
    global total_List
    for row in range(0, n):  # generate the full table
        list_temp = list(range(row*n+1, row*n+n+1))
        total_List.append(list_temp)
    (total_List[n-1])[n-1] = "$"  # replace the last one as '$'
    global place
    place = [n-1, n-1]  # to state the location of the space
    return total_List
    # mess it


def display(total_List):  # display the table
    for row in total_List:
        for column in row:
            print("%+3s" % (column), end=" ")  # to display on certain position
        print("\n", end="")


def operation(op):
    global n
    global total_List
    global place
    a = 0  # y-axis movement in coordinate
    b = 0  # x-axis movement in coordinate
    if op == 'up' and place[0] != n-1:
        a = 1
    if op == 'down' and place[0] != 0:
        a = -1
    if op == 'left' and place[1] != 0:
        b = -1
    if op == 'right' and place[1] != n-1:
        b = 1
    total_List[place[0]][place[1]] = total_List[place[0]+a][place[1]+b]
    total_List[place[0]+a][place[1]+b] = '$'  # change the position
    place[0] = place[0]+a
    place[1] = place[1]+b  # change the coordinate position of the '$'


n = 5  # determine the size of the table
place = [0, 0]  # to initialize location of the space
total_List=[]
initial_List = generating(n)  # generating the initial list
display(total_List)
while True:
    list_For_Judge = total_List
    operation(input('Select your operation: '))
    display(total_List)
    if list_For_Judge == total_List:
        print("Invalid Operation!")
