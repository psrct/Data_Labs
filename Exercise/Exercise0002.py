'''Exercise 00.02'''
def rainny(sites, minutes):
    '''ฝนตกไหม Indoor or Outdoor'''
    # hours = minutes/60
    if sites == "Indoor" and minutes >= 480:
        print(True)
    elif sites == "Outdoor" and minutes >= 240:
        print(True)
    else:
        print(False)
rainny(str(input()), float(input()))
