def generating(n):  # generating the initial table in order
    total_List = []
    for row in range(0, n):  # generate the full table
        list_temp = list(range(row*n+1, row*n+n+1))
        total_List.append(list_temp)
    (total_List[n-1])[n-1] = "$"  # replace the last one as '$'
    global place
    place = [n-1, n-1]  # to state the location of the space
    return total_List


def display(total_List):  # display the table
    for row in total_List:
        for column in row:
            print("%+3s" % (column), end=" ")  # to display on certain position
        print("\n", end="")


def operation(n):
    global total_List
    global place
    a = 0  # x-axis movement in coordinate
    b = 0  # y-axis movement in coordinate
    if n == 'up':
        a = 1
    if n == 'down':
        a = -1
    if n == 'left':
        b = -1
    if n == 'right':
        b = 1
    ((total_List[place[0]+a])[place[1]+b]), ((total_List[place[0]])[place[1]]
                                             ) = ((total_List[place[0]])[place[1]]), ((total_List[place[0]+a])[place[1]+b])  # change the position
    place[0] = place[0]+a
    place[1] = place[1]+b  # change the coordinate position of the '$'


place = [0, 0]  # to initialize location of the space
total_List = generating(5)
display(total_List)
while True:
    try:
        operation(input('Select your operation: '))
    except:
        print('Invalid operation!')
    display(total_List)
