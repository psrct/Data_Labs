'''Lab 02.05 Parentheses Matching'''

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

def is_parenthese_matching(expression):
    '''is_parenthese_match'''
    stackexpr = ArrayStack()
    check = True
    for i in expression:
        if i == "(":
            stackexpr.push(i)
        if i == ")":
            if stackexpr.pop() not in ["(", ")"]:
                check = False
    if stackexpr.size == 0 and check:
        print("Parentheses in", expression, "are matched")
        print(True)
    else:
        print("Parentheses in", expression, "are unmatched")
        print(False)
is_parenthese_matching(str(input()))
