'''Lab 07.01 Create BSTNode'''

class BSTNode:
    '''Class Binary search tree'''
    def __init__(self, data):
        '''init'''
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        '''getdata'''
        return self.data

    def set_data(self, data):
        '''setdata'''
        self.data = data

    def get_left(self):
        '''getleft'''
        return self.left

    def set_left(self, left):
        '''setleft'''
        self.left = left

    def get_right(self):
        '''getright'''
        return self.right

    def set_right(self, right):
        '''set right'''
        self.right = right

def main(num):
    '''main'''
    node = BSTNode(num)
    print(node.get_data())
    print(node.get_left())
    print(node.get_right())
main(int(input()))
