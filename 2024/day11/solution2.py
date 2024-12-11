from functools import lru_cache


class Stones:
    stones: list[int]

    def __init__(self, path: str):
        with open(path) as f:
            self.stones = [int(x.strip()) for x in f.read().strip().split(' ')]

    def blink(self):
        new_stones = []
        for stone in self.stones:
            new_stones += self.new_stone_state(stone)
        self.stones = new_stones

    @staticmethod
    @lru_cache(maxsize=1000000)
    def new_stone_state(stone: int) -> list[int]:
        if stone == 0:
            return [1]
        digits = str(stone)
        if len(digits) % 2 == 0:
            return [int(digits[:len(digits) // 2]), int(digits[len(digits) // 2:])]
        return [stone * 2024]

    def print(self):
        print(self.stones)

@lru_cache(maxsize=1000000)
def walk(stone, remaining_blinks: int):
    if remaining_blinks <= 0:
        return 1
    return sum([walk(x, remaining_blinks - 1) for x in Stones.new_stone_state(stone)])


def main():
    stones = Stones('input1.txt')
    res = sum([walk(x, 75) for x in stones.stones])
    print(f'result: {res}')


if __name__ == '__main__':
    main()
