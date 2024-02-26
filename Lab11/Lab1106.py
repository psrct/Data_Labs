'''Labs 11.06 Seats Number (Bubble Sort)'''
import json
def bubblesort(list1, last):
    '''BubbleSort'''
    compair = 0
    current = 0
    sortedd = False
    while current <= last and sortedd == False:
        walker = last
        sortedd = True
        while walker > current:
            if list1[walker][0] < list1[walker-1][0]:
                sortedd = False
                list1[walker], list1[walker-1] = list1[walker-1], list1[walker]
            elif list1[walker][0] == list1[walker-1][0]:
                if int(list1[walker][1:]) < int(list1[walker-1][1:]):
                    sortedd = False
                    list1[walker], list1[walker-1] = list1[walker-1], list1[walker]
            walker -= 1
            compair += 1
        current += 1
        print(list1)
    print("Comparison times:", compair)
bubblesort(json.loads(input()), int(input()))
