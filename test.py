sum = 0
for x in range(0, 4):
    for y in range(0, 3):
        if y <= x:
            sum = sum+(x+1)*(4-x)*(y+1)*(3-y)
print(sum)
