'''Exercise01.01- The Numbers Station I'''

def station():
    ''' 5 int(input())'''
    text_num = ""
    for _ in range(5):
        number = int(input())
        text_num += str(number)
    print(text_num)

station()
