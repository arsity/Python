def operation(n):
    global lockerList
    for lockerNumber in range(n-1, 100, n):
        lockerList[lockerNumber] = not lockerList[lockerNumber]


lockerList = []
for locker in range(0, 100):
    lockerList.append(False)
for student in range(1, 101):
    operation(student)
for index in range(0, 100):
    if lockerList[index]:
        lockerList[index] = 'Open'
    else:
        lockerList[index] = 'Closed'
count = 1
for locker in lockerList:
    if count % 10 == 0:
        print('%10s' % locker, end='\n')
    else:
        print('%10s' % locker, end=' ')
    count += 1
