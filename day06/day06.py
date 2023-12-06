import numpy as np
with open('day06/input.txt') as f:
    data = f.read().strip().split('\n')

class Races:

    def __init__(self):
        self.current = -1
        self.races = {}
        for l in data:
            key,values = l.split(':')
            value_list = list(map(int,values.split()))
            self.races[key.lower()] = value_list

    def __getitem__(self,index):
        return (self.races['time'][index],self.races['distance'][index])

    def __iter__(self):
        return self
    
    def items(self):
        return self.races.items()

    def __next__(self):
        if self.current<=len(self.races):
            self.current += 1
            return self.__getitem__(self.current)
        raise StopIteration
def hold(time_limit):
    distances = []
    for h in range (time_limit):
        remaining_time = time_limit-h
        distance = remaining_time*h
        distances.append(distance)
    return distances

def wins(distances,record):
    return np.sum(np.array(distances)>record)

def part2():
    time = int(data[0].split(':')[1].replace(' ',''))
    distance = int(data[1].split(':')[1].replace(' ',''))
    print(wins(hold(time),distance))
if __name__ == '__main__':
    races = Races()
    total = 1
    for time,max_distance in races:
        total*= wins(hold(time),max_distance)
    print(total)
    part2()


        

