import dataclasses
from collections import defaultdict
from functools import reduce
from operator import mul


@dataclasses.dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


class Game:
    height: int
    width: int
    robots: list[Robot]

    def __init__(self, path: str):
        with open(path) as f:
            self.robots = []
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                print(line)
                if line.startswith('h='):
                    hexpr, wexpr = line.split(' ')
                    self.height = int(hexpr.strip().split('=')[1])
                    self.width = int(wexpr.strip().split('=')[1])
                else:
                    pexpr, vexpr = line.split(' ')
                    pos = pexpr.split('=')
                    posx, posy = pos[1].split(',')
                    velocity = vexpr.split('=')
                    vx, vy = velocity[1].split(',')
                    self.robots.append(Robot(int(posx), int(posy), int(vx), int(vy)))

    def get_robot_position_at_time(self, r: Robot, t: int) -> (int, int):
        x = (r.x + r.vx * t) % self.width
        y = (r.y + r.vy * t) % self.height
        return x, y

    def count_result(self, t: int) -> int:
        robots: list[tuple[int, int]] = [self.get_robot_position_at_time(r, t) for r in self.robots]
        assert self.width % 2 == 1
        assert self.height % 2 == 1
        middle_x = self.width // 2
        middle_y = self.height // 2
        quadrants = defaultdict(lambda: 0)
        acc = 1
        for x, y in robots:
            if x == middle_x or y == middle_y:
                continue
            quadrants[(x < middle_x, y < middle_y)] += 1

        print(quadrants)
        return reduce(mul, quadrants.values())



def main():
    game = Game('input1.txt')
    print(f'result: {game.count_result(100)}')


if __name__ == '__main__':
    main()
