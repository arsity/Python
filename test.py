import random
fruitList = {}
for i in range(1,10):
    coordinate = (20*random.randint(-11, 11), 20*random.randint(-13, 9))
    fruitList['%s' % 'f'+str(i)]=coordinate
print(tuple(fruitList.values()))