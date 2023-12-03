class Map:
    def __init__(self, file: str):
        self.map = []
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                self.map.append(list(line))

    def get(self, x: int, y: int):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
            return ' ';
        else:
            return self.map[y][x]

    def is_character(self, x: int, y: int):
        c = self.get(x, y)
        result = c != ' ' and not c.isdigit() and c != '.'
        return result

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def get_neighbour_coords(self, x1: int, y1: int, x2: int, y2: int) -> set[tuple[int, int]]:
        result = set()
        for x in range(x1 - 1, x2 + 2):
            result.add((x, y1 - 1))
            result.add((x, y2 + 1))
        for y in range(y1 - 1, y2 + 2):
            result.add((x1 - 1, y))
            result.add((x2 + 1, y))
        return result

    def set(self, x: int, y: int, c: str):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
            return
        self.map[y][x] = c

    def is_at_least_one_neighbour_char(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        for x, y in self.get_neighbour_coords(x1, y1, x2, y2):
            if self.is_character(x, y):
                return True
        return False

    def find_numbers(self) -> list[tuple[int, int, int]]:
        result = []
        n_x = None
        n_y = None
        for y in range(0, len(self.map) + 1):
            for x in range(0, len(self.map[0]) + 1):
                if self.get(x, y).isdigit():
                    if n_x is None:  # start number recording
                        n_x, n_y = x, y
                    else:  # continue
                        pass
                else:
                    if n_x is None:
                        pass
                    else:
                        result.append((n_x, n_y, x - n_x))
                        n_x, n_y = None, None
        return result

    def get_number(self, x, y, l):
        return int((''.join(self.map[y]))[x: x + l])


def main():
    m = Map('input1.txt')
    m.print_map()
    adjacent_numbers = []
    for nx, ny, nl in m.find_numbers():
        if m.is_at_least_one_neighbour_char(nx, ny, nx + nl - 1, ny):
            adjacent_numbers.append(m.get_number(nx, ny, nl))

    print()
    print(sum(adjacent_numbers))


if __name__ == '__main__':
    main()
