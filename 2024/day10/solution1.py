import dataclasses
import itertools
from typing import Generator


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def key(self) -> (int, int):
        return self.x, self.y


class Map:
    m: list[list[int]]

    def height(self):
        return len(self.m)

    def width(self):
        return len(self.m[0])

    def __init__(self, path: str):
        with open(path) as f:
            self.m = []
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                self.m.append([int(x) for x in list(line)])

    def get(self, pos: Position):
        return self.m[pos.y][pos.x]

    def print(self):
        for y in range(0, self.height()):
            print(''.join([str(x) for x in self.m[y]]))

    def get_all_border_points(self) -> Generator[Position, None, None]:
        for x in range(0, self.width()):
            yield Position(x, 0)
            yield Position(x, self.height() - 1)

        for y in range(1, self.height() - 2):
            yield Position(0, y)
            yield Position(self.width() - 2, y)

    def get_all_trailheads(self) -> Generator[Position, None, None]:
        for x, y in itertools.product(range(0, self.width()), range(0, self.height())):
            pos = Position(x, y)
            if self.get(pos) == 0:
                yield pos

    def is_in_map(self, pos: Position):
        return 0 <= pos.x < self.width() and 0 <= pos.y < self.height()

    def get_4_sides(self, pos: Position) -> Generator[Position, None, None]:
        yield Position(pos.x + 1, pos.y)
        yield Position(pos.x - 1, pos.y)
        yield Position(pos.x, pos.y - 1)
        yield Position(pos.x, pos.y + 1)

    def get_moves(self, pos: Position) -> Generator[Position, None, None]:
        for pos in self.get_4_sides(pos):
            if self.is_in_map(pos):
                yield pos

    def walk(self, pos: Position, path: list[tuple[int, int]], result: list[list[tuple[int, int]]]):
        if pos in path:
            return
        path = path.copy()
        path.append(pos.key())
        if self.get(pos) == 9:
            # print(f"Found {pos} with {path}")
            result.append(path)
            return
        current_cell = self.get(pos)
        for move_pos in self.get_moves(pos):
            if self.get(move_pos) != current_cell + 1:
                continue
            self.walk(move_pos, path, result)


def main():
    m = Map('input1.txt')
    acc = 0
    for pos in m.get_all_trailheads():
        walk_result = []
        m.walk(pos, [], walk_result)
        acc += len(set([x[-1] for x in walk_result]))
    print(f'result: {acc}')


if __name__ == '__main__':
    main()
