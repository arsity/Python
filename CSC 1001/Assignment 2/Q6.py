import copy


def initialize(n):
    queenMatrix = []
    statusMatrix = []
    for row in range(n):
        queenMatrix.append(list(' '*n))
    for row in range(n):
        statusMatrix.append(list('0'*n))
    return queenMatrix, statusMatrix


def add(row, column, queenMatrix, statusMatrix, n):
    queenMatrix[row][column] = 'Q'

    for i in range(n):
        statusMatrix[row][i] = '1'
        statusMatrix[i][column] = '1'

    nw_Num = min(row, column)
    se_Num = n-1-max(row, column)
    ne_Num = min(row, n-1-column)
    sw_Num = n-1-max(row, n-1-column)

    for i in range(-nw_Num, se_Num+1):
        statusMatrix[row+i][column+i] = '1'
    for i in range(-sw_Num, ne_Num+1):
        statusMatrix[row-i][column+i] = '1'

    return queenMatrix, statusMatrix


def operation(queenMatrix, statusMatrix, n):
    initial_StatusMatrix = statusMatrix
    save_QueenMatrix = list('N'*n)
    save_StatusMatrix = list('N'*n)
    success_QueenMatrix = []
    row = 0
    retry_Attempt = 0
    while True:
        try:
            column_Index = statusMatrix[row].index(
                '0', statusMatrix[row].index('0')+retry_Attempt)
            retry_Attempt = 0
            queenMatrix, statusMatrix = add(
                row, column_Index, queenMatrix, statusMatrix, n)
            save_QueenMatrix[row] = copy.deepcopy(queenMatrix)
            save_StatusMatrix[row] = copy.deepcopy(statusMatrix)
            row += 1
        except:
            row -= 2
            statusMatrix = copy.deepcopy(save_StatusMatrix[row])
            queenMatrix = copy.deepcopy(save_QueenMatrix[row])
            retry_Attempt += 1
        if row > n-1:
            success_QueenMatrix.append(queenMatrix)
            mark_Column = queenMatrix[0].index('Q')
            if mark_Column == n-1:
                return success_QueenMatrix
            statusMatrix = initial_StatusMatrix
            for i in range(mark_Column+1):
                statusMatrix[0][i] = '2'


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
    success_List = operation(queenMatrix, statusMatrix, n)
    for i in success_List:
        display(i, n)


main(4)
