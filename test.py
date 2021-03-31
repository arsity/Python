sum = 0
for y in range(1, 5):
    for x in range(1, 3):
        sum = sum+(y-2.8125)**2*(x+y)/32
print(sum)
