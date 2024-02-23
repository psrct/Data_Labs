'''Labs 11.01 insertionSort()'''
import json
def insertionsort(list1, last):
    '''insertionSort'''
    current = 1
    count = 0
    while current <= last:
        hold = list1[current]
        walker = current -1
        while walker >= 0 and hold < list1[walker]:
            list1[walker +1] = list1[walker]
            walker -= 1
            count += 1
        if hold >= list1[walker] and walker >= 0:
            count += 1
        list1[walker + 1] = hold
        current += 1
        print(list1)
    print("Comparison times:", count)
insertionsort(json.loads(input()), int(input()))
