'''Labs 12.03 Radio Stations'''
class City:
    '''City'''
    def __init__(self, name, cities):
        '''init'''
        self.name = name
        self.cities = cities
 
    def get_name(self):
        '''getname'''
        return self.name
 
    def get_city(self):
        '''getcity'''
        return self.cities
 
import json
def findstations(allstations, numstation):
    '''findStations'''
    stationlist, newlist, staion, num = [], [], set(), 0
 
    for _ in range(numstation):
        stain = json.loads(input())
        stationlist.append(
            City(stain['Name'], stain['Cities'])
        )
    stationlist.sort(key=lambda x: len(x.get_city()), reverse=True)
    for j in stationlist:
        if len(newlist) == len(allstations):
            break
        for i in range((len(stationlist[num].get_city()))):
            word = j.get_city()[i]
            if word in allstations:
                if word in newlist:
                    continue
                else:
                    newlist.append(word)
                    staion.add(j.get_name())
                    for new in range(num+1, len(stationlist)):
                        if word in stationlist[new].get_city():
                            stationlist[new].get_city().remove(word)
                    stationlist.sort(key=lambda x: len(x.get_city()), reverse=True)
        num += 1
    staion = list(staion)
    print(sorted(staion))
findstations(json.loads(input()), int(input()))
