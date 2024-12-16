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
                    self.m.append(list(line))
                    if '@' in line:
                        self.robot = (line.index('@'), len(self.m) - 1)
                if line[0] in '<^v>':
                    self.moves += list(line)

    def try_to_move(self, x, y, direction: str) -> bool:
        tx, ty = self.get_target_pos(x, y, direction)
        target = self.get(tx, ty)
        is_robot = self.get(x, y) == '@'
        if target == '#':
            return False
        if target == 'O':
            try_to_move = self.try_to_move(tx, ty, direction)
            if try_to_move:
                self.set(tx, ty, self.get(x, y))
                self.set(x, y, '.')
                if is_robot:
                    self.robot = (tx, ty)

            return try_to_move
        if target == '@':
            assert False
        if target == '.':
            self.set(tx, ty, self.get(x, y))
            self.set(x, y, '.')
            if is_robot:
                self.robot = (tx, ty)
            return True
        assert False

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
                if self.get(x, y) == 'O':
                    acc += 100 * y  +x
        return acc


def main():
    game = Game('input1.txt')
    game.print()
    for m in game.moves:
        x, y = game.robot
        print(f'moving {x} {y} {m}')
        game.try_to_move(x, y, m)
        # game.print()
    game.print()
    print(f'result: {game.get_score()}')


if __name__ == '__main__':
    main()
