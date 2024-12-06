import dataclasses
from enum import Enum


class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def get_tuple(self) -> (int, int):
        return self.x, self.y


class Guard:
    position: Position
    direction: Direction
    path_cells: set[tuple[int, int]]

    def __init__(self, pos: Position, direction: Direction):
        self.position = pos
        self.direction = direction
        self.path_cells = {pos.get_tuple()}

    def turn_right(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
            return
        if self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
            return
        if self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
            return
        if self.direction == Direction.LEFT:
            self.direction = Direction.UP
            return

    def get_next_position(self):
        if self.direction == Direction.UP:
            return Position(self.position.x, self.position.y - 1)
        if self.direction == Direction.RIGHT:
            return Position(self.position.x + 1, self.position.y)
        if self.direction == Direction.DOWN:
            return Position(self.position.x, self.position.y + 1)
        if self.direction == Direction.LEFT:
            return Position(self.position.x - 1, self.position.y)

    def move(self, pos: Position):
        print(f'{self.position} -> {pos}')
        self.position = pos
        self.path_cells.add(pos.get_tuple())

    def __str__(self):
        return str(self.__dict__)


class Map:
    OBSTACLE = '#'
    map: list[str]
    guard: Guard

    def __init__(self, gmap: list[str], guard: Guard):
        self.map = gmap
        self.guard = guard

    def height(self):
        return len(self.map)

    def width(self):
        return len(self.map[0])

    def get(self, pos: Position) -> str:
        return self.map[pos.y][pos.x]

    def is_position_in_map(self, pos: Position) -> bool:
        is_in_map = 0 <= pos.x <= (self.width() - 1) and 0 <= pos.y <= (self.height() - 1)
        if not is_in_map:
            print(f"out of map {self.width()}x{self.height()}: {pos}. ")
        return is_in_map

    def is_position_obstacle(self, pos: Position) -> bool:
        is_obstacle = self.is_position_in_map(pos) and self.get(pos) == self.OBSTACLE
        if is_obstacle:
            print(f"if {pos} obstacle: {is_obstacle}")
        return is_obstacle

    def print(self):
        for y in range(0, self.height()):
            for x in range(0, self.height()):
                p = self.get(Position(x, y))
                if (x, y) in self.guard.path_cells:
                    # print(f'{self.guard.position.get_tuple()} in {self.guard.path_cells}')
                    p = '#'
                if self.guard.position.get_tuple() == (x, y):
                    p = '*'
                print(p, end='')
            print('')


def main():
    with open('input1.txt') as f:
        gmap = []
        guard_pos = Position(-1, -1)
        g = '^'
        for line in f:
            line = line.strip()
            gmap.append(line)
            if g in line:
                guard_pos.x = line.index(g)
                guard_pos.y = len(gmap) - 1
        guard = Guard(guard_pos, Direction.UP)
        gmap = Map(gmap, guard)

    while True:
        next_position = gmap.guard.get_next_position()
        # print(gmap.guard, next_position)
        if not gmap.is_position_in_map(next_position):
            break
        if gmap.is_position_obstacle(next_position):
            gmap.guard.turn_right()
            continue
        gmap.guard.move(next_position)
        # print(gmap.guard)
    gmap.print()
    print(f'result: {len(gmap.guard.path_cells)}')


if __name__ == '__main__':
    main()
