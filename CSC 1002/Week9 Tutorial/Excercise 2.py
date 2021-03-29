tripleEvenElements = list(
    map(lambda x: x**3, filter(lambda x: x % 2 == 0, range(1, 11))))
print(tripleEvenElements)
