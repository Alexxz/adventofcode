class FS:
    mem: list[int | None] = []
    max_file_id: int

    def __init__(self, path: str):
        with open(path) as f:
            block_mem = f.read().strip()
        for i, v in enumerate(list(block_mem)):
            intv = int(v)
            if i % 2 == 0:
                file_id = i // 2
                self.mem += [file_id] * intv
                self.max_file_id = file_id
            else:
                self.mem += [None] * intv

    def get_by_index(self, i: int) -> int | None:
        return self.mem[i]

    def set_by_index(self, i: int, v: int | None):
        self.mem[i] = v

    def get_control_sum(self) -> int:
        return sum([i * v for i, v in enumerate(self.mem) if v is not None])

    def print(self):
        print(self.get_as_str())

    def get_as_str(self):
        return ''.join([('.' if x is None else '#') for x in self.mem])

    def get_file_by_id(self, n: int) -> (int, int):
        file_end = None
        for i in range(len(self.mem) - 1, 0, -1):
            val = self.get_by_index(i)
            if file_end is None and val is None:
                continue
            if file_end is None and val == n:
                file_end = i
            if file_end is not None and val != n:
                file_pos = i + 1
                return file_pos, file_end - file_pos + 1
        return None, None

    def get_leftmost_empty_space_of_length(self, length) -> int | None:
        search_string = '.' * length
        mem_str = self.get_as_str()
        if search_string not in mem_str:
            return None
        return mem_str.index(search_string)

    def defrarment(self):
        for file_id in range(self.max_file_id, 0, -1):
            print(f'file_id: {file_id}')
            (fpos, flen) = self.get_file_by_id(file_id)
            if fpos is None:
                continue
            new_pos = self.get_leftmost_empty_space_of_length(flen)
            if new_pos is None or new_pos > fpos:
                continue
            for i in range(0, flen):
                self.set_by_index(new_pos + i, self.get_by_index(fpos + i))
                self.set_by_index(fpos + i, None)


def main():
    fs = FS('input1.txt')
    fs.defrarment()
    print(f'result: {fs.get_control_sum()}')


if __name__ == '__main__':
    main()
