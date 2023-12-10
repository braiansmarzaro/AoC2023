with open('day05/input.txt') as f:
    data = f.read().strip().split('\n')
    f.seek(0)
    data2 = f.read().strip().split('\n\n')

#print(data2)
class Mapping:
    def __init__(self) -> None:
        self.seeds = data[0][6:].split()
        self.seed_to_soil = data2[1].split('\n')[1:]
        self.soil_to_fertilizer = data2[2].split('\n')[1:]
        self.fertilizer_to_water = data2[3].split('\n')[1:]
        self.water_to_light = data2[4].split('\n')[1:]
        self.light_to_temperature = data2[5].split('\n')[1:]
        self.temperature_to_humidity = data2[6].split('\n')[1:]
        self.humidity_to_location = data2[7].split('\n')[1:]

        self.locations = [self.get_location(x) for x in self.seeds]
        print(min(self.locations))
        # Part 2
    def is_seed(self,value):
        for s in range(0,len(self.seeds),2):
            if int(self.seeds[s])<=int(value)<=int(self.seeds[s])+int(self.seeds[s+1]):
                return True
        return False
        
    def map_source_destination(self,lista,source_value):
        """Finds the value in destination related to the source. If source value not listed, return itself.

        Args:
            line (_type_): _description_
            source_value (_type_): _description_

        Returns:
            _type_: _description_
        """
        source_value = int(source_value)
        def map_line(line):

            destination,source,length = map(int,line.split())
            source_range = source+length
            if source<=source_value<=source_range:
                pos = source_value-source
                return destination+pos
            return None
        
        for l in (lista):
            result = map_line(l)
            if result is not None:
                return result
        
        return source_value

    def get_location(self,source_value):
        
        value = self.map_source_destination(self.seed_to_soil,source_value)
        value = self.map_source_destination(self.soil_to_fertilizer,value)
        value = self.map_source_destination(self.fertilizer_to_water,value)
        value = self.map_source_destination(self.water_to_light,value)
        value = self.map_source_destination(self.light_to_temperature,value)
        value = self.map_source_destination(self.temperature_to_humidity,value)
        value = self.map_source_destination(self.humidity_to_location,value)
        print('Step done7')
        return value
if __name__ == "__main__":
    mapping = Mapping()