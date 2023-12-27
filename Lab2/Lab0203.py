'''Lab 02.03 Student Groups'''

class ArrayStack:
    '''Class ArrayStack'''
    def __init__(self):
        '''init'''
        self.size = 0
        self.data = []

    def push(self, data):
        '''push input_data in stack'''
        data = str(data)
        if data.isdigit():
            data = int(data)
        elif data.replace(".", "", 1).isdigit():
            data = float(data)
        self.data.append(data)
        self.size += 1

    def pop(self):
        '''pop'''
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
        else:
            output = self.data.pop()
            self.size -= 1
            return output

    def is_empty(self):
        '''is_empty'''
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        '''StackTop'''
        if self.size != 0:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
    def get_size(self):
        '''size'''
        return self.size

    def print_stack(self):
        '''print'''
        print(self.data)

def main(group, students):
    '''main'''
    STACK = ArrayStack()
    lis = []
    for _ in range(students):
        STACK.push(input())
    for _ in range(group):
        lis.append(ArrayStack())
    while True:
        if STACK.is_empty() == False:
            for i in range(group):
                poppy = STACK.pop()
                lis[i].push(poppy)
        else:
            break
    for i in range(len(lis)):
        print("Group "+ str(i+1) + ": ", end="")
        print(*(lis[i].data),sep=", ")

main(int(input()), int(input()))
