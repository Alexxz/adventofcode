import re

left = []
right = []
with open('input1.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        l, r = re.split(r'\s+', line)
        left.append(int(l))
        right.append(int(r))

left = sorted(left)
right = sorted(right)

assert len(left) == len(right)

acc = 0
for i in range(0, len(left)):
    acc += abs(left[i] - right[i])

print(f'result: {acc}')
