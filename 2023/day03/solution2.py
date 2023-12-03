import dataclasses


@dataclasses.dataclass
class Gear:
    x: int
    y: int
    length: int


class Map:
    def __init__(self, file: str):
        self.map = []
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                self.map.append(list(line))

    def get(self, x: int, y: int):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
            return ' '
        else:
            return self.map[y][x]

    def is_character(self, x: int, y: int):
        c = self.get(x, y)
        result = c != ' ' and not c.isdigit() and c != '.'
        return result

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    @staticmethod
    def get_neighbour_coords(gear: Gear) -> set[tuple[int, int]]:
        x1, y1, x2, y2 = gear.x, gear.y, gear.x + gear.length - 1, gear.y
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

    def is_at_least_one_neighbour_char(self, gear: Gear) -> bool:
        for x, y in self.get_neighbour_coords(gear):
            if self.is_character(x, y):
                return True
        return False

    def find_gears(self) -> list[Gear]:
        result = []
        n_x = None
        n_y = None
        for y in range(0, len(self.map) + 1):
            for x in range(0, len(self.map[0]) + 1):
                if self.get(x, y).isdigit():
                    if n_x is None:  # start number recording
                        n_x, n_y = x, y
                else:
                    if n_x is None:
                        pass
                    else:
                        result.append(Gear(n_x, n_y, x - n_x))
                        n_x, n_y = None, None
        return result

    def get_number(self, gear: Gear) -> int:
        return int((''.join(self.map[gear.y]))[gear.x: gear.x + gear.length])


def get_local_gears(all_gears: list[Gear], gear: Gear) -> list[Gear]:
    result = []
    for i_gear in all_gears:
        if abs(i_gear.y - gear.y) <= 2 and not (i_gear.x == gear.x and i_gear.y == gear.y):
            result.append(i_gear)
    return result


def pair(a, b) -> tuple[int, int]:
    if a < b:
        return a, b
    else:
        return b, a


def main():
    m = Map('input1.txt')
    m.print_map()
    gears = m.find_gears()
    gear_pairs = set()
    for gear in gears:
        local_gears = get_local_gears(gears, gear)
        for neig_x, neig_y in m.get_neighbour_coords(gear):
            if m.get(neig_x, neig_y) != '*':
                continue
            asterisk_x = neig_x
            asterisk_y = neig_y
            for local_gear in local_gears:
                # print('checking', asterisk_x, asterisk_y, 'with', m.get_number(lg_x, lg_y, lg_l))
                if (asterisk_x, asterisk_y) in m.get_neighbour_coords(local_gear):
                    print('gear', m.get_number(gear), 'is next to', m.get_number(local_gear))
                    gear_pairs.add(pair(m.get_number(gear), m.get_number(local_gear)))

    print(gear_pairs)
    print(sum([a * b for a, b in gear_pairs]))


if __name__ == '__main__':
    main()
