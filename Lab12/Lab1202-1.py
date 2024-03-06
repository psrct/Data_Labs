'''Labs 12.02 (1) Item Class'''

class Item:
    '''Itme class'''
    def __init__(self, name, price, weight):
        '''init'''
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        '''getname'''
        return self.__name

    def get_price(self):
        '''getprice'''
        return self.__price

    def get_weight(self):
        '''getweight'''
        return self.__weight

    def get_cost(self):
        '''get Cost'''
        return self.__price // self.__weight
def main():
    '''main'''
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
