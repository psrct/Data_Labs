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
    name = [
        "Walter", "Skyler", "Jesse", "Saul",
        "Mike", "Hank", "Marie",
        "Kim", "Gustavo", "Salamanca"
    ]


    def print_status():
        """Print all stacks"""
        print("This is stack 1 (%d): " % stack1.get_size(), end='')
        stack1.print_stack()
        print("This is stack 2 (%d): " % stack2.get_size(), end='')
        stack2.print_stack()
        print("This is stack 3 (%d): " % stack3.get_size(), end='')
        stack3.print_stack()
        print()


    stack1 = ArrayStack()
    stack2 = ArrayStack()
    stack3 = ArrayStack()
    for _ in range(len(name) // 2):
        stack1.push(name.pop())
        stack2.push(name.pop())
    print_status()

    while not stack1.is_empty() and not stack2.is_empty():
        stack3.push(stack1.get_stack_top())
        stack3.push(stack2.pop())
    print_status()

    for _ in range(stack3.get_size() + 1):
        stack3.pop()
    print_status()

    while not stack1.is_empty():
        tempall = stack1.pop()
        stack2.push(tempall)
        stack3.push(tempall)
    print_status()

    while not stack2.is_empty():
        tempall = stack2.pop()
        print(tempall)
    print()
    print_status()

    while not stack3.is_empty():
        stack2.push(stack3.pop())
    print_status()
main()
