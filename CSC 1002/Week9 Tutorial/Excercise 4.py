from functools import reduce


a = 4
b = 16465786978


def translate(n):
    digitList = ''
    while n != 0:
        digitList += str(n % 2)
        n = n//2
    return digitList[::-1]


a_2 = translate(a)
b_2 = translate(b)

if len(a_2) > len(b_2):
    len(b_2) = (len(a_2)-len(b_2))*'0'+len(b_2)
else:
    len(a_2) = (len(b_2)-len(a_2))*'0'+len(a_2)

