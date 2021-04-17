class flower:
    def __init__(self) -> None:
        self.name = 'rose'
        self.number = 3
        self.price = 10.00

    def name(self):
        print(self.name)

    def setName(self):
        while True:
            name = input('Please enter the name of flower: ')
            if len(name) != 0:
                self.name = name
                break

    def number(self):
        print(self.number)

    def setNumber(self):
        while True:
            number = input('Please enter the number of flower: ')
            if number.isnumeric() and int(number) >= 0:
                self.number = int(number)
                break
            print('Please enter a non-negative integer.')

    def price(self):
        print(self.price)

    def setPrice(self):
        while True:
            price = input('Please enter the price of flower: ')
            try:
                price = float(price)
                if price <= 0:
                    print('Please enter a postive float.')
                    continue
                self.price = price
                break
            except:
                print('Please enter a positive float.')


def main():
    a = flower()
    a.name()
    a.number()
    a.price()
    a.setName()
    a.setNumber()
    a.setPrice()
    a.name()
    a.number()
    a.price()


main()
