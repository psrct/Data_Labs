'''Lab 07.02 Binary Search Tree (Preorder, Insert)'''

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

class BST:
    '''Class Binary search tree'''
    def __init__(self):
        '''init'''
        self.root = None

    def get_root(self):
        '''get root'''
        return self.root

    def set_root(self, root):
        '''set root'''
        self.root = root

    def insert(self, data):
        '''Inset data'''
        if self.root is None:
            self.set_root(BSTNode(data))
        else:
            pnew = self.root
            while True:
                if pnew.data > data:
                    if pnew.get_left() is None:
                        pnew.set_left(BSTNode(data))
                        break
                    else:
                        pnew = pnew.get_left()
                elif pnew.data < data:
                    if pnew.get_right() is None:
                        pnew.set_right(BSTNode(data))
                        break
                    else:
                        pnew = pnew.get_right()

    def preorder(self):
        '''preorder'''
        def print_node(node):
            '''print node'''
            if node != None:
                print("->", node.data, end=" ")
                print_node(node.get_left())
                print_node(node.get_right())
        print_node(self.root)

def main():
    """Data Structures and Algorithms Lab Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
