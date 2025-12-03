import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sum = 0
with open('input.1') as f:
    for line in f:
        line = line.strip()
        found = False
        for a in range(9, -1, -1):
            if found:
                break
            a_pos = line[:-1].find(str(a))
            if a_pos == -1:
                continue
            for b in range(9, -1, -1):
                if found:
                    break
                b_pos = line[a_pos+1:].rfind(str(b))
                if b_pos != -1:
                    sum += a*10 + b
                    print(line)
                    print(line[:a_pos], line[a_pos:a_pos+b_pos+1], line[a_pos+b_pos+1:])
                    print(a*10 + b)
                    found = True

print(f'joiltage: {sum}')
# 17204 too low
# 17432