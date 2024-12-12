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
        print(f'{region.value} area {region.area()} perimeter {region.perimeter()}')
        acc += region.area() * region.perimeter()
    print(f'result: {acc}')


if __name__ == '__main__':
    main()
