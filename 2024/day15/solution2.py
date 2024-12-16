import copy


class Game:
    m: list[list[str]]
    moves: list[str]
    robot: tuple[int, int]

    def __init__(self, path: str):
        self.m = []
        self.moves = []
        self.robot = (-1, -1)
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                if line.startswith('#'):
                    replaces = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
                    for k in replaces.keys():
                        line = line.replace(k, replaces[k])
                    self.m.append(list(line))
                    if '@' in line:
                        self.robot = (line.index('@'), len(self.m) - 1)
                if line[0] in '<^v>':
                    self.moves += list(line)

    def get_moving_sequence(self, x: int, y: int, direction: str) \
            -> list[tuple[int, int, str]] | None:
        cell = self.get(x, y)
        if cell == '@':
            nx, ny = self.get_target_pos(x, y, direction)
            moving_sequence = [(x, y, '.'), (nx, ny, '@')]
            pre_seq = self.get_moving_sequence(nx, ny, direction)
            if pre_seq is None:
                return None
            return pre_seq + moving_sequence
        if cell == '#':
            return None
        if cell == '[':
            lnx, lny = self.get_target_pos(x, y, direction)
            left_seq = self.get_moving_sequence(lnx, lny, direction)
            if left_seq is None:
                return None
            rnx, rny = self.get_target_pos(x + 1, y, direction)
            right_seq = self.get_moving_sequence(rnx, rny, direction)
            if right_seq is None:
                return None
            return left_seq + right_seq + [(lnx, lny, '['), (rnx, rny, ']'), (x, y, '.'), (x + 1, y, '.')]
        if cell == ']':
            if direction == '>':
                seq = self.get_moving_sequence(x+1, y, direction)
                if seq is None:
                    return None
                return seq + [(x, y, '['), (x + 1, y, ']'), (x-1, y, '.')]
            elif direction == '<':
                seq = self.get_moving_sequence(x - 2, y, direction)
                if seq is None:
                    return None
                return seq + [(x - 2, y, '['), (x - 1, y, ']'), (x, y, '.')]
            else:
                return self.get_moving_sequence(x - 1, y, direction)
        if cell == '.':
            return []
        assert False

    def try_to_move(self, x, y, direction: str) -> bool:
        seq = self.get_moving_sequence(x, y, direction)
        # print(seq)
        if seq is None:
            return False
        new_map = copy.deepcopy(self.m)
        for x, y, v in seq:
            if v == '.':
                new_map[y][x] = v
        for x, y, v in seq:
            if v != '.':
                new_map[y][x] = v
        self.m = new_map
        self.update_robot_position()
        return True

    def get_target_pos(self, x: int, y: int, direction: str) -> (int, int):
        if direction == '^':
            return x, y - 1
        if direction == '>':
            return x + 1, y
        if direction == 'v':
            return x, y + 1
        if direction == '<':
            return x - 1, y
        assert False

    def get(self, x: int, y: int) -> str:
        return self.m[y][x]

    def set(self, x: int, y: int, v: str):
        self.m[y][x] = v

    def print(self):
        for line in self.m:
            print(''.join(line))

    def height(self):
        return len(self.m)

    def width(self):
        return len(self.m[0])

    def get_score(self) -> int:
        acc = 0
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if self.get(x, y) == '[':
                    acc += 100 * y + x
        return acc

    def update_robot_position(self):
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                if self.get(x, y) == '@':
                    self.robot = (x, y)
                    return


def main():
    game = Game('input1.txt')
    game.print()
    for m in game.moves:
        x, y = game.robot
        print(f'moving {x} {y} {m}')
        moved = game.try_to_move(x, y, m)
        # print(moved)
        # game.print()
    game.print()
    print(f'result: {game.get_score()}')


if __name__ == '__main__':
    main()
