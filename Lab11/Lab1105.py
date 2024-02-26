'''Labs 11.05 Seats Number (Selection Sort)'''
import json
def selectionsort(list1, last):
    '''selectionsort'''
    count = 0
    current = 0
    while current != last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if list1[walker][0] < list1[smallest][0]:
                smallest = walker
            elif list1[walker][0] == list1[smallest][0]:
                if int(list1[walker][1:]) < int(list1[smallest][1:]):
                    smallest = walker
            count += 1
            walker += 1
        list1[current], list1[smallest] = list1[smallest], list1[current]
        current += 1
        print(list1)
    print("Comparison times:", count)
selectionsort(json.loads(input()), int(input()))
