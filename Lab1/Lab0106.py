'''Lab 01.06 - Elevator'''

class Elevator:
    '''Class Elevator'''
    def __init__(self, max_floor):
        '''Attributes'''
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        '''go to '''
        if floor <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor!")

    def report_current_floor(self):
        '''report'''
        print(self.current_floor)

def main():
    '''main'''
    lift = Elevator(int(input()))
    while True:
        floor1 = input()
        if floor1 == "Done":
            lift.report_current_floor()
            break
        else:
            lift.go_to_floor(int(floor1))
main()
