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

    def new_stone_state(self, stone: int) -> list[int]:
        if stone == 0:
            return [1]
        digits = str(stone)
        if len(digits) % 2 == 0:
            return [int(digits[:len(digits) // 2]), int(digits[len(digits) // 2:])]
        return [stone * 2024]

    def print(self):
        print(self.stones)


def main():
    stones = Stones('input1.txt')
    stones.print()
    for i in range(0, 25):
        stones.blink()
    print(f'result: {len(stones.stones)}')

if __name__ == '__main__':
    main()
