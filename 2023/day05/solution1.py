from pprint import pprint


class Range:
    def __init__(self, dest_start: int, source_start: int, range_length: int):
        self.dest_starts = dest_start
        self.source_starts = source_start
        self.range = range_length

    def convert(self, source: int) -> int | None:
        if self.source_starts <= source <= self.source_starts + self.range:
            return self.dest_starts + (source - self.source_starts)
        return None


class GameMaps:
    maps: dict[str, list[Range]]
    seeds: list[int]

    def __init__(self):
        self.maps = dict()
        self.seeds = []


def input(file: str):
    result = GameMaps()
    current_map = None
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()

            if line == '':
                continue

            if line.startswith('seeds:'):
                result.seeds = [int(x.strip()) for x in line.split(':')[1].strip().split(' ')]
                continue

            if line.endswith(':'):
                current_map = line.split(':')[0]
                continue

            x1, x2, x3 = [int(x) for x in line.split(' ')]
            if current_map not in result.maps:
                result.maps[current_map] = []

            result.maps[current_map].append(Range(x1, x2, x3))

    return result


def convert(source: int, ranges: list[Range]) -> set[int]:
    result = set()
    for r in ranges:
        converted = r.convert(source)
        if converted is not None:
            result.add(converted)

    return result if len(result) > 0 else {source}


def main():
    maps = input('input1.txt')
    locations = []
    for seed in maps.seeds:
        print('seed', seed)
        for soil in convert(seed, maps.maps['seed-to-soil map']):
            print('soil', soil)
            for fertilizer in convert(soil, maps.maps['soil-to-fertilizer map']):
                print('fertilizer', fertilizer)
                for water in convert(fertilizer, maps.maps['fertilizer-to-water map']):
                    print('water', water)
                    for light in convert(water, maps.maps['water-to-light map']):
                        for temperature in convert(light, maps.maps['light-to-temperature map']):
                            for humidity in convert(temperature, maps.maps['temperature-to-humidity map']):
                                for location in convert(humidity, maps.maps['humidity-to-location map']):
                                    print(location)
                                    locations.append(location)
    print('min', min(locations))


if __name__ == '__main__':
    main()
