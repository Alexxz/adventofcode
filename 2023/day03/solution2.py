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


def get_local_gears(all_gears, gx, gy, gl):
    result = []
    for x, y, l in all_gears:
        if abs(y - gy) <= 2 and not (x == gx and y == gy):
            result.append((x, y, l))
    return result


def pair(a, b) -> tuple[int, int]:
    if a < b:
        return a, b
    else:
        return b, a


def main():
    m = Map('input1.txt')
    m.print_map()
    adjacent_numbers = []
    gears = m.find_numbers()
    gear_pairs = set()
    for gear in gears:
        x, y, l = gear
        local_gears = get_local_gears(gears, x, y, l)
        for neig_x, neig_y in m.get_neighbour_coords(x, y, x + l - 1, y):
            if m.get(neig_x, neig_y) != '*':
                continue
            asterisk_x = neig_x
            asterisk_y = neig_y
            # print('processing', asterisk_x, asterisk_y, 'for', m.get_number(x, y, l))
            # print('local gears ', local_gears)
            for lg_x, lg_y, lg_l in local_gears:
                # print('checking', asterisk_x, asterisk_y, 'with', m.get_number(lg_x, lg_y, lg_l))
                if (asterisk_x, asterisk_y) in m.get_neighbour_coords(lg_x, lg_y, lg_x + lg_l - 1, lg_y):
                    print('gear', m.get_number(x, y, l), 'is next to', m.get_number(lg_x, lg_y, lg_l))
                    gear_pairs.add(pair(m.get_number(x, y, l), m.get_number(lg_x, lg_y, lg_l)))

    print(gear_pairs)
    print(sum([a * b for a, b in gear_pairs]))


if __name__ == '__main__':
    main()
