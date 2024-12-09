import dataclasses
from collections import defaultdict


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def key(self) -> tuple[int, int]:
        return self.x, self.y


class Map():
    m: list[str]
    antennas: defaultdict[str, list[Position]]

    def __init__(self, path: str):
        with open(path) as f:
            self.m = list()
            self.antennas = defaultdict(lambda: [])
            for y, line in enumerate(f):
                line = line.strip()
                if line == '':
                    continue
                self.m.append(line)
                for x in range(0, len(line)):
                    if line[x].isalnum():
                        self.antennas[line[x]].append(Position(x, y))

    def get_width(self):
        return len(self.m[0])

    def get_height(self):
        return len(self.m)

    def get_resonance_points(self):
        for freq in self.antennas.keys():
            antnnas = self.antennas[freq]
            for a in antnnas:
                for b in antnnas:
                    if a.key() == b.key():
                        continue
                    yield Position(b.x + (b.x - a.x), b.y + (b.y - a.y))

    def is_in_map(self, pos: Position):
        return 0 <= pos.x < self.get_width() and 0 <= pos.y < self.get_height()


def main():
    m = Map('input1.txt')
    points = set()
    for pos in m.get_resonance_points():
        if m.is_in_map(pos):
            points.add(pos.key())
    print(f'result: {len(points)}')


if __name__ == '__main__':
    main()