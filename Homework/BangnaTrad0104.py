'''Exercise 01.04 - Bangna Trad'''

def roads(kilometers):
    '''Bangna Trad'''
    if kilometers >= 0 and kilometers <= 5.032:
        print("Bangkok")
    elif kilometers > 5.032 and kilometers <= 35.477:
        print("Samut Prakarn")
    elif kilometers > 35.477 and kilometers <= 52.900:
        print("Chachoengsao")
    elif kilometers > 52.900 and kilometers <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")

roads(float(input()))
