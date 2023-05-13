import numpy as np


def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return np.array(sum)


def main():
    max = 0

    for i in range(4192305):
        if sum_digits(i) > max:
            max = sum_digits(i)

    print(max)


if __name__ == "__main__":
    main()
