import re

mem = open('input1.txt').read(10000000)

r = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(r, mem)
acc = 0
for m in matches:
    a, b = re.findall(r'\d{1,3}', m)
    acc += int(a) * int(b)
print(mem)
print(matches)
print(f'result: {acc}')