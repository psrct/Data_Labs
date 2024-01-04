"""Lab 02.04 Copy Stack"""

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

def copy_stack(stack1, stack2):
    '''CopyStack'''
    freestack = ArrayStack()
    for _ in range(stack2.get_size()):
        stack2.pop()
    for _ in range(stack1.get_size()):
        out = stack1.pop()
        freestack.push(out)
    for _ in range(freestack.get_size()):
        out = freestack.pop()
        stack1.push(out)
        stack2.push(out)
    del freestack

def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()


STACK1_ = ArrayStack()
STACK2_ = ArrayStack()


STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
    STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(
    STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
      TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))
