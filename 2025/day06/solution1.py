import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers = []
with open("input.1") as f:
    for line in f:
        line = line.strip()
        if '+' in line or '*' in line:
            signs = re.split(r'\s+', line)
            continue
        ns = re.split(r'\s+', line)
        if ns[0] == '':
            n.pop(0)
        n = [int(x) for x in ns]
        numbers.append(n)


results = []
for i in range(len(numbers[0])):
    result = 0 if signs[i] == '+' else 1
    for n in range(len(numbers)):
        if signs[i] == '+':
            result += numbers[n][i]
        else:
            result *= numbers[n][i]
    results.append(result)
# print(results)
print(sum(results))
