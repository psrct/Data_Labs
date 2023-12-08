'''Lab 01.05 - Point'''

class Point:
    '''Point'''
    def __init__(self, x=0, y=0):
        '''Atti'''
        self.set_coordinates(x, y)

    def set_coordinates(self, xxx, yyy):
        '''set'''
        self.xxx = xxx
        self.yyy = yyy

    def get_coordinates(self):
        '''get'''
        return (self.xxx, self.yyy)

    def calculate_distance(self, other_point):
        '''calculate'''
        return ((other_point.xxx - self.xxx)**2 + (other_point.yyy - self.yyy)**2) ** 0.5

def main():
    '''main'''
    number1 = Point(float(input()), float(input()))
    number2 = Point(float(input()), float(input()))
    print("%.2f" %(number1.calculate_distance(number2)))
main()
