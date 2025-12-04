import os

from poetry.console.commands import self

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Map:
    def __init__(self):
        self.m = []
        with open('input.1') as f:
            for line in f:
                line = line.strip()
                self.m.append(line)

    def width(self) -> int:
        return len(self.m[0])

    def height(self) -> int:
        return len(self.m)

    def get(self, pos):
        x, y = pos
        if x < 0 or x >= self.width() or y < 0 or y >= self.height():
            return '.'
        return self.m[y][x]

    def get_adjacent_list(self, pos: tuple[int, int]):
        x, y = pos
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), ]

    def get_neighbors(self, pos: tuple[int, int]):
        return list(map(lambda x:  self.get(x), self.get_adjacent_list(pos)))

    def get_all_pos(self):
        for x in range(self.width()):
            for y in range(self.height()):
                yield (x, y)

    def get_adjacent_rolls_number(self, pos):
        neighbors = self.get_neighbors(pos)
        rolls_number = len([x for x in neighbors if x == '@'])
        return rolls_number

    def get_accessible_rolls(self):
        result = []
        for pos in self.get_all_pos():
            if self.get(pos) != '@':
                continue
            if self.get_adjacent_rolls_number(pos) < 4:
                result.append(pos)
        return result

    def print_map(self):
        for y in range(self.height()):
            for x in range(self.width()):
                print(self.get((x, y)), end='')
            print()

    def print_accessible_map(self):
        accessible_rolls = self.get_accessible_rolls()
        for y in range(self.height()):
            for x in range(self.width()):
                pos = (x, y)
                c = self.get(pos)
                if pos in accessible_rolls:
                    c = 'x'
                print(c, end='')
            print()


m = Map()
m.print_accessible_map()
print(f'Number of available rolls: {len(m.get_accessible_rolls())}')

