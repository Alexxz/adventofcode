import numpy as np


def get_number_of_presents(i: int):
    N = i
    tst = np.arange(1, N)
    divisors = tst[np.mod(N, tst) == 0]
    s = N + sum([x for x in divisors if x * 50 >= N])
    return s * 11


def main():
    input = int(open('input1.txt').read())
    #2772000 too high
    #2494800 too high
    #900900 not connect should we go down?
    i = 900900
    while True:
        i -= 1
        presents = get_number_of_presents(i)
        if i % 1000 == 0:
            print(f"processing: {i} - {presents}")
        if presents >= input:
            print(f'result? {i} <---------------------')
            # return


if __name__ == '__main__':
    main()
