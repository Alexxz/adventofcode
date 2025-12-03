import os
import timeit

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def generate_best_solution(rs: str, length: 12) -> str:
    res = ""
    idx = 0
    while len(res) < length:
        last_index = -(length - len(res)) + 1
        field_for_lookup = rs[idx:last_index] if last_index != 0 else rs[idx:]
        # find leftmost max
        for x in range(9, 0, -1):
            x_pos = field_for_lookup.find(str(x))
            if x_pos < 0:
                continue
            res = res + str(x)
            idx = idx + x_pos+1
            if len(res) == length:
                return res
            break
    raise Exception('No solution found')

assert generate_best_solution('987654321111111', 12) == '987654321111'
assert generate_best_solution('811111111111119', 12) == '811111111119'
assert generate_best_solution('234234234234278', 12) == '434234234278'
assert generate_best_solution('818181911112111', 12) == '888911112111'

assert generate_best_solution('123456789123', 12) == '123456789123'
assert generate_best_solution('1234567891231', 12) == '234567891231'
assert generate_best_solution('9999999999991', 12) == '999999999999'
assert generate_best_solution('9999999999919', 12) == '999999999999'
assert generate_best_solution('9199999999999', 12) == '999999999999'
assert generate_best_solution('1999999999999', 12) == '999999999999'

assert generate_best_solution('1999999999999', 4) == '9999'
assert generate_best_solution('9999', 4) == '9999'
assert generate_best_solution('9989', 3) == '999'
assert generate_best_solution('9889', 3) == '989'
assert generate_best_solution('7889', 3) == '889'
assert generate_best_solution('8789', 3) == '889'
assert generate_best_solution('8189', 3) == '889'
assert generate_best_solution('1191', 3) == '191'
assert generate_best_solution('1119', 3) == '119'
assert generate_best_solution('1198', 3) == '198'
assert generate_best_solution('1982', 3) == '982'
assert generate_best_solution('9919', 3) == '999'
assert generate_best_solution('9119', 3) == '919'
assert generate_best_solution('9819', 3) == '989'
assert generate_best_solution('9189', 3) == '989'
assert generate_best_solution('9189', 3) == '989'
assert generate_best_solution('1234', 3) == '234'
assert generate_best_solution('12345', 3) == '345'
assert generate_best_solution('1234544444', 3) == '544'
assert generate_best_solution('213141516171', 3) == '671'
assert generate_best_solution('818284', 3) == '888'
assert generate_best_solution('1111111111111118111111182333184', 3) == '888'
assert generate_best_solution('51515151551515151515', 5) == '55555'
assert generate_best_solution('111111111888', 3) == '888'
assert generate_best_solution('1111111118881', 3) == '888'
assert generate_best_solution('11111111181818111', 3) == '888'
assert generate_best_solution('1818181', 3) == '888'
assert generate_best_solution('9788987789777777777', 12) == '999777777777'

def bank_to_joltage(s: str ) -> int:
    return int(generate_best_solution(s, 12))

with open('input.1') as f:
    s = 0
    input=[]
    for line in f:
        line = line.strip()
        input.append(line)
        result = generate_best_solution(line, 12)
        s += int(result)
    print(f'joiltage: {s}')

# 171055976599737 wrong
# correct 173065202451341

tries = 2000
timeit_timeit = timeit.timeit(lambda: sum(map(bank_to_joltage, input)), number=tries)
print(f"timeit: {round(timeit_timeit * 1000 / tries, 2)} ms")
print("res: ", sum(map(bank_to_joltage, input)))

