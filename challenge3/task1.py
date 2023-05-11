import numpy as np
import task2 as t2

k = np.array([1, 1, 1])


def convert_to_base_10(u):
    u_base_10 = 0
    for i in range(len(u)):
        u_base_10 += u[i] * 2 ** (len(u) - 1 - i)
    return np.array(u_base_10)


def convert_to_base_2(t):
    t_base_2 = []
    while t:
        t_base_2.append(t % 2)
        t //= 2
    return np.array(t_base_2)


def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return np.array(sum)


def tag_computation(u, k):
    return np.array(u * k)


def get_u():
    print("-----------------------")
    print("Insert the message one bit at the time. (Escape with 'q')")
    esc = 0
    u = []
    while esc <= 10:
        u_i = input("Insert bit: ")
        u.append(int(u_i))
        esc += 1
    u = np.array(u)
    print("u = ", u)
    print("-----------------------")


"""
def verify_tag(x, k):
    u_1 = x[0 : len(u)]
    print("u = ", u_1)
    print("k = ", k)
    t = tag_computation(
        sum_digits(convert_to_base_10(u_1)), sum_digits(convert_to_base_10(k))
    )
    t = convert_to_base_2(t)
    return t
"""


def verify_tag_task2(x, k):
    u_1 = x[0 : len(t2.u)]
    print("u = ", u_1)
    print("k = ", k)
    t = tag_computation(
        sum_digits(convert_to_base_10(u_1)), sum_digits(convert_to_base_10(k))
    )
    t = convert_to_base_2(t)
    return t


def main():
    u = np.array([1, 0, 1])
    print("u = ", u)
    print("k = ", k)
    t = tag_computation(
        sum_digits(convert_to_base_10(u)), sum_digits(convert_to_base_10(k))
    )
    t = convert_to_base_2(t)
    print("t = ", t)
    x = np.concatenate((u, t))
    print("x = ", x)
    print("-----------------------")
    print("Verify the Tag.")
    t_prime = verify_tag(x, k)
    print("Is the tag correct? ", np.array_equal(t_prime, t))


if __name__ == "__main__":
    main()
