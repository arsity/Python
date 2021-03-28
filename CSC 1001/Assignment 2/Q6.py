def initialize():
    matrix = []
    matrix.append(list('Q'*8))
    for n in range(0, 8):
        matrix.append(list(' '*8))
    return matrix


def display():
    count = 1
    for row in matrix:
        print('|', end='')
        for column in row:
            if count % 8 == 0:
                print(column, end='|\n')
            else:
                print(column, end='|')
            count += 1


matrix = initialize()
display()
