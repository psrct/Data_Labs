'''Lab 01.02 - Max…Min…Avg'''
import json

def calculate(lis):
    '''calculate'''
    bigest = lis[0]
    smallest = lis[0]
    aver = 0
    for i in lis:
        if i > bigest:
            bigest = i
        if i < smallest:
            smallest = i
        aver += i
    aver /= len(lis)
    aver = round(aver, 2)
    bigest = round(bigest, 2)
    smallest = round(smallest, 2)
    list1 = [bigest, smallest, aver]
    tupleout = tuple(list1)
    print(tupleout)

calculate(json.loads(input()))
