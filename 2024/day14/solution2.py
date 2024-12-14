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
        for x, y in robots:
            if x == middle_x or y == middle_y:
                continue
            quadrants[(x < middle_x, y < middle_y)] += 1

        print(quadrants)
        return reduce(mul, quadrants.values())

    def get_robots_in_time(self, t: int) -> dict[tuple[int, int], bool]:
        robots_dict = {}
        for r in self.robots:
            robots_dict[self.get_robot_position_at_time(r, t)] = True
        return robots_dict

    def get_neighbours_score(self, robots: dict[tuple[int, int], bool]) -> int:
        acc = 0
        for rx, ry in robots.keys():
            acc += robots.get((rx - 1, ry - 1), 0)
            acc += robots.get((rx - 1, ry - 0), 0)
            acc += robots.get((rx - 1, ry + 1), 0)
            acc += robots.get((rx - 0, ry - 1), 0)
            acc += robots.get((rx - 0, ry + 1), 0)
            acc += robots.get((rx + 1, ry - 1), 0)
            acc += robots.get((rx + 1, ry - 0), 0)
            acc += robots.get((rx + 1, ry + 1), 0)
        return acc

    def print_at_time(self, t: int):
        robots_dict = self.get_robots_in_time(t)
        print(f'Time: {t} seconds')
        for y in range(0, self.height):
            line = ''
            for x in range(0, self.width):
                line += '#' if robots_dict.get((x, y)) is True else ' '
            line += '|'
            print(line)


def main():
    game = Game('input1.txt')
    # print(f'result: {game.count_result(100)}')
    max_score = 0
    for t in range(0, 10000):
        robots = game.get_robots_in_time(t)
        score = game.get_neighbours_score(robots)
        if score > max_score:
            print(f'Score: {score}')
            game.print_at_time(t)
            max_score = score


if __name__ == '__main__':
    main()
