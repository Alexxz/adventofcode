import re

with open('input1.txt', 'r') as f:
    acc=[]
    for line in f:
        line = line.strip()
        print(f'Line: {line}')
        line = re.sub(r'[^0-9]', '', line)
        digits = line[0] + line[-1]
        print(digits)
        acc.append(int(digits))

    print(sum(acc))