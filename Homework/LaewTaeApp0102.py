'''Exercise 01.02 - Laew Tae App V.1'''
import math
import json

class LaewTaeApp:
    '''Laew Tae App'''
    def __init__(self, list_food, timerandom):
        '''Attributes'''
        self.food = list_food
        self.time = timerandom

    def random_foods(self, lis1, count):
        '''Random'''
        math.random(lis1)
        count += 1

    def show_food(self, lis1):
        '''list of foods'''
        lis = sorted(lis1)
        print(*lis)

def main():
    '''main'''
    listfood = json.loads(input())
    count = 0
    app = LaewTaeApp(listfood, int(input()))
    app.random_foods(listfood, count)
    app.show_foods(listfood)

main()
