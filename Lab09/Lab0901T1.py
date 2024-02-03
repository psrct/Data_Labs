'''Labs 09.01 - Summation (Type 1)'''

def summation(num):
    '''Summation (Type 1)'''
    total = 0
    for i in range(1, num+1):
        total += i
    print(total)
summation(int(input()))
