import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input.1') as f:
    body = f.read().replace('\n', '')
    ranges = body.split(',')
    ranges = [r.split('-') for r in ranges]


def match(s: str) -> bool:
    l = len(s)
    for n in range(1, l // 2 + 1):
        if l % n != 0:
            continue
        sublines = {tuple(s[i:i+n]) for i in range(0, len(s), n)}
        if len(sublines) == 1:
            return True
    return False


sum = 0
for r in ranges:
    a, b = r[0], r[1]
    for i in range(int(a), int(b) + 1):
        s = str(i)
        m = match(s)
        # print(f'{i} - {match}')
        if m:
            sum += i
print(f'sum: {sum}')
