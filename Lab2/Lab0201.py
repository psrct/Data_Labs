'''Lab 02.01 Stack (Create Stack)'''

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

def main():
    '''main'''
    stack1 = ArrayStack()

    stack1.push("100")
    stack1.push(100)
    stack1.push("3.14")
    stack1.push(3.14)
    stack1.push("66.4a")
    stack1.push("Ackerman")

    stack1.print_stack()

    print(stack1.get_size())
    var1 = stack1.pop()
    print(var1)
    stack1.print_stack()
    print(stack1.get_size())

    while not stack1.is_empty():
        print(stack1.pop())

    print()
    print(stack1.pop())
    print(stack1.get_stack_top())
    print(var1)

main()
