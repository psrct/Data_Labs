'''Lab 07.05 Binary Search Tree (Cases 1, 2, 3)'''

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

    def delete(self, data):
        '''Delete'''
        def deleted(root, data):
            '''deleted'''
            if root is None:
                print("Delete Error, {0} is not found in Binary Search Tree.".format(data))
                return None
            else:
                if root.get_data() > data:
                    item = deleted(root.get_left(), data)
                    root.set_left(item)
                    return root
                elif root.get_data() < data:
                    item = deleted(root.get_right(), data)
                    root.set_right(item)
                    return root
                else:
                    if root.get_left() != None:
                        return root.get_left()
                    else:
                        return root.get_right()
        pnew = deleted(self.root, data)
        if data == self.root.get_data():
            self.set_root(pnew)

    def find_min(self):
        '''Find the minimum'''
        if self.root != None:
            pnew = self.root
            while True:
                if pnew.get_left() is None:
                    return pnew.get_data()
                else:
                    pnew = pnew.get_left()

    def find_max(self):
        '''Find the maximum'''
        if self.root != None:
            pnew = self.root
            while True:
                if pnew.get_right() is None:
                    return pnew.get_data()
                else:
                    pnew = pnew.get_right()

    def is_empty(self):
        '''empty BST'''
        if self.root is None:
            return True
        else:
            return False

    def preorder(self):
        '''preorder'''
        def print_node(node):
            '''print node'''
            if node != None:
                print("->", node.data, end=" ")
                print_node(node.get_left())
                print_node(node.get_right())
        print_node(self.root)

    def inorder(self):
        '''inorder'''
        def print_nodein(node):
            '''print node'''
            if node != None:
                print_nodein(node.get_left())
                print("->", node.data, end=" ")
                print_nodein(node.get_right())
        print_nodein(self.root)

    def postorder(self):
        '''postorder'''
        def print_nodepost(node):
            '''print node'''
            if node != None:
                print_nodepost(node.get_left())
                print_nodepost(node.get_right())
                print("->", node.data, end=" ")
        print_nodepost(self.root)

    def traverse(self):
        ''' traverse'''
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print("")
        print('Inorder: ', end='')
        self.inorder()
        print("")
        print('Postorder: ', end='')
        self.postorder()
        print("")

def main():
    """Data Structures and Algorithms Lab Binary Search Tree"""
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
