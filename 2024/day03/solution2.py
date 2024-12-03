import re

mem = open('input1.txt').read(10000000)
print(mem)
# mem.replace("\n", '')

r = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = re.findall(r, mem)
acc = 0
en = True
for m in matches:
    if m.startswith("don't"):
        en = False
        continue
    if m.startswith("do()"):
        en = True
        continue
    if en:
        a, b = re.findall(r'\d{1,3}', m)
        acc += int(a) * int(b)
print(f'result: {acc}')
