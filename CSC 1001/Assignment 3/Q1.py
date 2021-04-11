class Flower:
    def __init__(self, name='rose', number=1, price=10.00):
        self.name = name
        self.number = number
        self.price = price

    def setName(self):
        name = input('Please enter the name of the flower: ')
        self.name = name

    def name(self):
        return self.name

    def setNumber(self):
        while True:
            number = input('Please enter the number of the flower: ')
            if number.isdecimal() and int(number) >= 0:
                self.number = int(number)
                break
            else:
                print('Please input a non-negative integer.')

    def number(self):
        return self.number

    def setPrice(self):
        while True:
            price = input('Please enter the price of the flower: ')
            try:
                price = float(price)
                if float < 0:
                    print('Please enter a non-negative float.')
                    continue
                else:
                    self.price = price
            except:
                print('Please enter a non-negative float.')

    def price(self):
        return self.price
