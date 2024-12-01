import re
from collections import defaultdict

left = []
rcount = defaultdict(lambda: 0)
with open('input1.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        l, r = re.split(r'\s+', line)
        l = int(l)
        left.append(l)
        r = int(r)
        rcount[r] += 1

acc = 0
for l in left:
    acc += l * rcount[l]

print(f'result: {acc}')
