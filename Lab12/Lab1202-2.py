'''Labs 12.02 (2) Knapsack'''

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

def knapsack(amount, itemlist):
    '''knapsack function'''
    most, total, weightt = 0, 0, 0
    newlist = itemlist.copy()
    newlist.sort(key = lambda k : k.get_cost())
    newlist.reverse()
    for i in itemlist:
        print(i.get_name(), i.get_cost())
    print("________________")
    for j in newlist:
        print(j.get_name(), j.get_cost())
    print("{} -> {} kg -> {} THB")
    print("===============================")
    print("Total: %d THB" %total)

def main():
    '''main'''
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)

main()
