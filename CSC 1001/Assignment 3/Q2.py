

class polynomial:
    def __init__(self, polynomial='0'):
        polynomialList = polynomial.split('+')
        polynomialList = tuple(
            filter(lambda x: not x.isnumeric(), polynomialList))


    def __str__(self):
        return self.answer


print(polynomial(input('Please enter your polynomial in standard algebraic notation:\n')))
