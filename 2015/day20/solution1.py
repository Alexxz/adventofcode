import numpy as np


def get_number_of_presents(i: int):
    N = i
    tst = np.arange(1, N)
    divisors = tst[np.mod(N, tst) == 0]
    s = N + sum(divisors)
    return s * 10


def main():
    input = int(open('input1.txt').read())
    i = 0
    while True:
        i += 100
        if i % 10000 == 0:
            print(f"processing: {i}")
        presents = get_number_of_presents(i)
        if presents >= input:
            print(f'result: {i}')
            return


if __name__ == '__main__':
    main()
