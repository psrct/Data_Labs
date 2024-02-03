'''Labs 09.03 - Calculator'''

def calculator(number):
    '''Calculator'''
    total = 0
    for i in range(1, number+1):
        total += len(str(i)) + 1
    print(total)
calculator(int(input()))
