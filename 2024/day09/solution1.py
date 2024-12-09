class FS:
    mem: list[int | None] = []

    def __init__(self, path: str):
        with open(path) as f:
            block_mem = f.read().strip()
        for i, v in enumerate(list(block_mem)):
            intv = int(v)
            if i % 2 == 0:
                file_id = i // 2
                self.mem += [file_id] * intv
            else:
                self.mem += [None] * intv

    def get_by_index(self, i: int) -> int | None:
        return self.mem[i]

    def set_by_index(self, i: int, v: int | None):
        self.mem[i] = v

    def get_control_sum(self) -> int:
        return sum([i * v for i, v in enumerate(self.mem) if v is not None])

    def print(self):
        print(''.join([('.' if x is None else str(x)) for x in self.mem]))

    def defrarment(self):
        i = 0
        j = len(self.mem) - 1
        while self.get_by_index(j) is None:
            j -= 1
        while i < j:
            if self.get_by_index(i) is None:
                self.set_by_index(i, self.get_by_index(j))
                self.set_by_index(j, None)
                while self.get_by_index(j) is None:
                    j -= 1
            i += 1


def main():
    fs = FS('input1.txt')
    fs.print()
    fs.defrarment()
    fs.print()
    print(f'result: {fs.get_control_sum()}')


if __name__ == '__main__':
    main()
