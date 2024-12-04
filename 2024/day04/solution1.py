m = []
with open('input1.txt') as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            continue
        m.append(list(l))


def generate_lines(matrix):
    for row in matrix:
        yield row


def regenerate_lines_reverse(gen):
    for row in gen:
        rev = row[::-1]
        yield row
        yield rev


def generate_columns(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    for col in range(0, ncols):
        res = []
        for row in range(0, nrows):
            res.append(matrix[row][col])
        yield res


def generate_diagonal(matrix):  # /
    nrows = len(matrix)
    ncols = len(matrix[0])
    for r in range(0, nrows):
        ix = 0
        iy = r
        res = []
        while 0 <= ix < ncols and 0 <= iy < nrows:
            res.append(matrix[iy][ix])
            ix += 1
            iy -= 1
        yield res
    for r in range(1, ncols):
        ix = r
        iy = nrows - 1
        res = []
        while 0 <= ix < ncols and 0 <= iy < nrows:
            res.append(matrix[iy][ix])
            ix += 1
            iy -= 1
        yield res


def generate_back_diagonal(matrix):  # \
    nrows = len(matrix)
    ncols = len(matrix[0])
    for r in range(ncols - 1, 0, -1):
        ix = r
        iy = 0
        res = []
        while 0 <= ix < ncols and 0 <= iy < nrows:
            res.append(matrix[iy][ix])
            ix += 1
            iy += 1
        yield res
    for r in range(0, ncols):
        ix = 0
        iy = r
        res = []
        while 0 <= ix < ncols and 0 <= iy < nrows:
            res.append(matrix[iy][ix])
            ix += 1
            iy += 1
        yield res


def generate_all_lines(m):
    for row in regenerate_lines_reverse(generate_lines(m)):
        yield row
    for row in regenerate_lines_reverse(generate_columns(m)):
        yield row
    for row in regenerate_lines_reverse(generate_diagonal(m)):
        yield row
    for row in regenerate_lines_reverse(generate_back_diagonal(m)):
        yield row


cnt = 0
for r in generate_all_lines(m):
    cnt += len(''.join(r).split('XMAS')) - 1

print(f'result: {cnt}')