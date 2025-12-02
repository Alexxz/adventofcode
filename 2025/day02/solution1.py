import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('input.1') as f:
    body = f.read().replace('\n', '')
    ranges = body.split(',')
    ranges = [r.split('-') for r in ranges]

sum = 0
for r in ranges:
    a, b = r[0], r[1]
    for i in range(int(a), int(b) + 1):
        # match = re.match(r'(.)\1+|(.{2,}?)\2+', str(i))
        s = str(i)
        match = len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]
        # print(f'{i} - {match}')
        if match:
            sum += i
print(f'sum: {sum}')
