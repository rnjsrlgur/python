class Airplane:
    def __init__(self, price, color):
        self.price = price
        self.color = color

    def print_price(self):
        print(self.price)

    def print_color(self):
        print(self.color)

airplane1 = Airplane(1000, 'red')
airplane2 = Airplane(2000, 'green')
airplane3 = Airplane(3000, 'blue')
airplane4 = Airplane(4000, 'purple')
airplane5 = Airplane(5000, 'pink')

print(f'airplane1.color = {airplane1.color}, airplane1.price = {airplane1.price}')
print(f'airplane2.color = {airplane2.color}, airplane2.price = {airplane2.price}')
print(f'airplane3.color = {airplane3.color}, airplane3.price = {airplane3.price}')
print(f'airplane4.color = {airplane4.color}, airplane4.price = {airplane4.price}')
print(f'airplane5.color = {airplane5.color}, airplane5.price = {airplane5.price}')