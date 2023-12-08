'''Lab 01.01 - Is_Even'''

def is_even(number):
    '''Lab 01.01 - Is_Even'''
    listeven = ["0", "2", "4", "6", "8"]
    if number[(len(number)-1)] in listeven:
        print(True)
    else:
        print(False)

is_even(str(input()))
