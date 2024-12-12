import dataclasses
from collections.abc import Generator


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def get_4_neighbours(self) -> Generator['Position', None, None]:
        yield Position(self.x + 1, self.y)
        yield Position(self.x - 1, self.y)
        yield Position(self.x, self.y + 1)
        yield Position(self.x, self.y - 1)

    def key(self) -> (int, int):
        return self.x, self.y

    def is_neighbour(self, pos: 'Position') -> bool:
        for neighbour_pos in self.get_4_neighbours():
            if neighbour_pos.key() == pos.key():
                return True
        return False


@dataclasses.dataclass
class Side:
    pos_in: Position
    pos_out: Position

    def is_close_sided(self, side: 'Side'):
        return self.pos_in.is_neighbour(side.pos_in) and self.pos_out.is_neighbour(side.pos_out)


@dataclasses.dataclass
class Region:
    value: str
    cells: set[tuple[int, int]]

    def area(self) -> int:
        return len(self.cells)

    def perimeter(self) -> int:
        perimeter = 0
        for x, y in self.cells:
            pos = Position(x, y)
            for neighbour_pos in pos.get_4_neighbours():
                if neighbour_pos.key() not in self.cells:
                    perimeter += 1
        return perimeter

    def get_all_sides(self) -> list[Side]:
        sides = []
        for x, y in self.cells:
            pos = Position(x, y)
            for neighbour_pos in pos.get_4_neighbours():
                if neighbour_pos.key() not in self.cells:
                    sides.append(Side(pos, neighbour_pos))
        return sides

    def get_number_of_sides(self):
        all_sides = self.get_all_sides()
        group_sides = self.group_sides(all_sides)
        # print(f'{all_sides} => {group_sides}')
        return len(group_sides)

    def group_sides(self, sides: list[Side]) -> list[list[Side]]:
        sides = sides.copy()
        groups = []
        current_group: list[Side] | None = None
        while len(sides) > 0:
            if current_group is None:
                current_group = [sides.pop()]
                continue
            collapsed = False
            for group_el in current_group:
                for i in range(0, len(sides)):
                    if group_el.is_close_sided(sides[i]):
                        current_group.append(sides[i])
                        del sides[i]
                        collapsed = True
                        break
            if collapsed:
                continue
            groups.append(current_group)
            current_group = None
            continue
        if current_group is not None:
            groups.append(current_group)
        return groups


class Cell:
    value: str
    is_processed: False
    region: Region | None

    def __init__(self, value: str):
        self.value = value
        self.is_processed = False
        self.region = None


class Map:
    m: list[list[Cell]]
    regions: list[Region]

    def height(self) -> int:
        return len(self.m)

    def width(self) -> int:
        return len(self.m[0])

    def all_cells(self) -> Generator[Position, None, None]:
        for x in range(0, self.width()):
            for y in range(0, self.height()):
                yield Position(x, y)

    def get(self, pos: Position):
        return self.m[pos.y][pos.x]

    def reset_processed(self):
        for pos in self.all_cells():
            self.get(pos).is_processed = False

    def get_unprocessed(self) -> Generator[Position, None, None]:
        for pos in self.all_cells():
            if not self.get(pos).is_processed:
                yield pos

    def is_pos_in_map(self, pos: Position):
        return 0 <= pos.x < self.width() and 0 <= pos.y < self.height()

    def calculate_regions(self):
        self.reset_processed()
        self.regions = []
        for pos in self.all_cells():
            cell = self.get(pos)
            if cell.region is None:
                region = self.processed_region(pos)
                self.regions.append(region)

    def processed_region(self, pos: Position) -> Region:
        region = Region(self.get(pos).value, set())
        self.processed_region_rec(pos, region)
        return region

    def processed_region_rec(self, pos: Position, region: Region) -> None:
        cell = self.get(pos)
        cell.is_processed = True
        region.cells.add(pos.key())
        cell.region = region
        for neighbour_pos in pos.get_4_neighbours():
            if not self.is_pos_in_map(neighbour_pos):
                continue
            neighbour_cell = self.get(neighbour_pos)
            if neighbour_cell.is_processed:
                continue
            if neighbour_cell.value == cell.value:
                self.processed_region_rec(neighbour_pos, region)

    def __init__(self, path: str):
        self.m = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                cells = []
                for c in list(line):
                    cells.append(Cell(c))
                self.m.append(cells)
        self.calculate_regions()


def main():
    gmap = Map('input1.txt')
    gmap.reset_processed()
    print(f'located: {len(gmap.regions)} regions')
    acc = 0
    for region in gmap.regions:
        # print(f'processing region {region.value}')
        print(f'{region.value} area {region.area()} sides {region.get_number_of_sides()}')
        acc += region.area() * region.get_number_of_sides()
    print(f'result: {acc}')


if __name__ == '__main__':
    main()
