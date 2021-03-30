def initialize(n):
    queenMatrix = []
    statusMatrix = []
    for row in range(0, n):
        queenMatrix.append(list(' '*n))
    for row in range(0, n):
        statusMatrix.append(list('0'*n))
    return queenMatrix, statusMatrix


def add(row, column, queenMatrix, statusMatrix, n):
    queenMatrix[row][column] = 'Q'
    
    for i in range(0, n):
        statusMatrix[row][i] = '1'
        statusMatrix[i][column] = '1'

    nw_Num = min(row, column)
    se_Num = n-1-max(row, column)
    ne_Num = min(row, n-1-column)
    sw_Num = n-1-max(row, n-1-column)




def display(queenMatrix, n):
    count = 1
    for row in queenMatrix:
        print('|', end='')
        for column in row:
            if count % n == 0:
                print(column, end='|\n')
            else:
                print(column, end='|')
            count += 1


def main(n):
    queenMatrix, statusMatrix = initialize(n)
    add(3, 2, queenMatrix, statusMatrix, n)

    display(queenMatrix, n)


main(8)
