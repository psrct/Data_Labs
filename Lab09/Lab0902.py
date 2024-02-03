'''Labs 09.02 - isIntersect(A, B, C)'''
import json
def isintersect(list1, list2, list3):
    '''isIntersect'''
    check = False
    for i in list1:
        if i in list2 and i in list3:
            check = True
            break
    print(check)
isintersect(json.loads(str(input())), json.loads(str(input())), json.loads(str(input())))
