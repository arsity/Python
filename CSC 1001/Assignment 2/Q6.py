def initialize():
    queenMatrix = []
    statusMatrix = []
    for row in range(0, 8):
        queenMatrix.append(list(' '*8))
    for row in range(0, 8):
        statusMatrix.append(list('0'*8))
    return queenMatrix, statusMatrix


def display(queenMatrix):
    count = 1
    for row in queenMatrix:
        print('|', end='')
        for column in row:
            if count % 8 == 0:
                print(column, end='|\n')
            else:
                print(column, end='|')
            count += 1


def main():
    queenMatrix, statusMatrix = initialize()

    display(queenMatrix)


main()
