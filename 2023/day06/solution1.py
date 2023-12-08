import dataclasses
import re


@dataclasses.dataclass
class Race:
    time: int
    distance: int


def get_input(file: str) -> list[Race]:
    result = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Time'):
                times = re.split(' +', line)[1:]
            if line.startswith('Distance'):
                distances = re.split(' +', line)[1:]
    for t, d in zip(times, distances):
        result.append(Race(time=int(t), distance=int(d)))

    return result


def main():
    races = get_input('input1.txt')
    print(races)
    result = 1
    for race in races:
        options = 0
        for i in range(0, race.time+1):
            speed = i
            distance = (race.time - i) * speed
            # print(f'hold {i}  speed {speed} distance {distance} target {race.distance}')
            if distance > race.distance:
                options += 1
        print(f'race {race} options {options}')
        result *= options

    print(f'answer {result}')

if __name__ == '__main__':
    main()
