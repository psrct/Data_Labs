'''Lab 05.05 Singly Linked List (Delete)'''

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

    def insert_before(self, back, front):
        '''insert_before'''
        if self.head == None:
            print("Cannot insert, %s does not exist." %back)
        else:
            pnew1 = self.head
            pnew2 = self.head.get_next()
            if pnew1.get_data() == back:
                temp0 = DataNode(front)
                self.head = temp0
                temp0.set_next(pnew1)
                self.count += 1
            else:
                while pnew2 != None and pnew2.get_data() != back:
                    pnew2 = pnew2.get_next()
                    pnew1 = pnew1.get_next()
                if pnew2 == None:
                    print("Cannot insert, %s does not exist." %back)
                else:
                    temp0 = DataNode(front)
                    pnew1.set_next(temp0)
                    temp0.set_next(pnew2)
                    self.count += 1

    def delete(self, data):
        '''delete'''
        if self.head == None:
            print("Cannot delete, %s does not exist." %data)
        else:
            pnew1 = self.head
            pnew2 = self.head.get_next()
            if pnew1.get_data() == data:
                self.head = pnew2
                del pnew1
                self.count -= 1
            else:
                while pnew2 != None and pnew2.get_data() != data:
                    pnew2 = pnew2.get_next()
                    pnew1 = pnew1.get_next()
                if pnew2 == None:
                    print("Cannot delete, %s does not exist." %data)
                else:
                    pnew1.set_next(pnew2.get_next())
                    del pnew2
                    self.count -= 1

LIST1_ = SinglyLinkedList()
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    elif CONDI_ == "B":
        LIST1_.insert_before(*DATA_.split(", "))
    elif CONDI_ == "D":
        LIST1_.delete(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()
