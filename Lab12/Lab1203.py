'''Labs 12.03 Radio Stations'''
class City:
    '''City'''
    def __init__(self, name, cities):
        '''init'''
        self.name = name
        self.cities = cities

    def get_name(self):
        return self.name

    def get_cities(self):
        return self.cities

import json
def findStations(allstations, numstation):
    '''findStations'''
    stationlist = []
    for _ in range(numstation):
        stain = json.loads(input())
        stationlist.append(
            City(stain['Name'], stain['Cities'])
        )
    stationlist.sort(key=lambda x: len(x.get_cities()), reverse=True)
    
    # for i in stationlist:
    #     print(i.get_name(), i.get_cities())

findStations(json.loads(input()), int(input()))
