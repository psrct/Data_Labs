'''Lab 05.03  Singly Linked List (Insert Front)'''

class DataNode:
    '''DataNode'''
    def __init__(self, data=None):
        '''init'''
        self.__data = data
        self.__next = None

    def get_data(self):
        '''return data'''
        return self.__data

    def set_data(self, data):
        '''set data'''
        self.__data = data

    def get_next(self):
        '''return .next'''
        return self.__next

    def set_next(self, nexter):
        '''set .next'''
        self.__next = nexter

class SinglyLinkedList:
    '''SinglyLinkedList'''
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        '''traverse'''
        if self.head == None:
            print("This is an empty list.")
        else:
            pnew = self.head
            while pnew.get_next() != None:
                print(pnew.get_data(), end=" -> ")
                pnew = pnew.get_next()
            print(pnew.get_data())

    def insert_last(self, data):
        '''insert_last'''
        if self.head == None:
            self.head = DataNode(data)
        else:
            pnew = self.head
            while pnew.get_next() != None:
                pnew = pnew.get_next()
            pnew.set_next(DataNode(data))
        self.count += 1

    def insert_front(self, data):
        '''insert_front'''
        pnew = self.head
        first = DataNode(data)
        self.head = first
        first.set_next(pnew)
        self.count += 1

    # def insert_before(node, data):
    #     '''insert_before'''

    # def delete(data):
    #     '''delete'''

LIST1_ = SinglyLinkedList()
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()
