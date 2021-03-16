# 找到2至N的所有质数
n = int(input("Integer:"))
a = []
for x in range(2, n+1):
    flag = False
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            flag = True
            break
    if flag == False:
        a.append(x)
print(a)
