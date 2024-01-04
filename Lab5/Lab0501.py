'''Lab 05.01 Create DataNode'''

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
        '''set .nexter'''
        self.__next = nexter

def main(nextt):
    '''main'''
    node = DataNode()
    node.set_data(nextt)
    print(node.get_data())
    print(node.get_next())
main(str(input()))
