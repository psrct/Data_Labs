'''Lab 01.04 - Rectangle'''

class Rectangle:
    '''Class'''
    def __init__(self, height, width):
        '''_'''
        self.height = height
        self.width = width

    def calculate_area(self):
        '''_'''
        total = self.height * self.width
        return total

    def calculate_perimeter(self):
        '''_'''
        total = 2 * (self.height + self.width)
        return total

def main():
    '''calculate'''
    rectan = Rectangle(float(input()), float(input()))
    condition = str(input())
    if condition == "area":
        result = rectan.calculate_area()
    else:
        result = rectan.calculate_perimeter()
    print("%.2f" %result)

main()
