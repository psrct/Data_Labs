'''Labs 11.04 Seats Number (Insertion Sort)'''
import json
def insertionsort(list1, last):
    '''insertionSort'''
    current = 1
    count = 0
    while current <= last:
        hold = list1[current]
        walker = current -1
        while walker >= 0 and hold[0] < list1[walker][0]:
            list1[walker + 1] = list1[walker]
            walker -= 1
            count += 1
        while hold[0] >= list1[walker][0] and walker >= 0:
            if hold[0] == list1[walker][0] and int(hold[1:]) < int(list1[walker][1:]):
                list1[walker + 1] = list1[walker]
                walker -= 1
                count += 1
            else:
                count += 1
                break
        list1[walker + 1] = hold
        current += 1
        print(list1)
    print("Comparison times:", count)
insertionsort(json.loads(input()), int(input()))
