'''Lab 01.03 - SwapVar'''

def convert_string_to_tuples(text_in):
    '''Swapvar'''
    values = text_in.strip('()').split(', ')
    list1 = list(map(float, values))
    list1 = list1[1], list1[0]
    return tuple(list1)

print(convert_string_to_tuples(input()))
