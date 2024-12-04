m = []
with open('input1.txt') as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            continue
        m.append(list(l))


def get(matrix, x, y):
    nrows = len(matrix)
    ncols = len(matrix[0])
    if 0 <= x < ncols and 0 <= y < nrows:
        return matrix[y][x]
    else:
        return '.'


def if_x_mas(matrix, x, y):
    d1 = f"{get(matrix, x - 1, y - 1)}{get(matrix, x, y)}{get(matrix, x + 1, y + 1)}"
    rd1 = d1[::-1]
    d2 = f"{get(matrix, x - 1, y + 1)}{get(matrix, x, y)}{get(matrix, x + 1, y - 1)}"
    rd2 = d2[::-1]
    return "MAS" in [d1, rd1] and 'MAS' in [d2, rd2]


def count_x_max(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    acc = 0
    for x in range(0, ncols):
        for y in range(0, nrows):
            if if_x_mas(matrix, x, y):
                acc += 1
    return acc


print(f'result: {count_x_max(m)}')
