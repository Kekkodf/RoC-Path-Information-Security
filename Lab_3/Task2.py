import numpy as np

k = np.array([1, 1, 1])
x = [1, 0, 1, 0, 0, 1, 1, 1, 0]
u = [1, 0, 1, 0, 0]
t = [1, 1, 1, 0]

def convert_to_base_10(u):
    u_base_10 = 0
    for i in range(len(u)):
        u_base_10 += u[i]*2**(len(u)-1-i)
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

def tag_computation(u,k):
    return np.array(u*k)

def verify_tag_task2(x, k):
    u_1 = x[0 : len(u)]
    print("u = ", u_1)
    print("k = ", k)
    t = tag_computation(
        sum_digits(convert_to_base_10(u_1)), sum_digits(convert_to_base_10(k))
    )
    t = convert_to_base_2(t)
    return t

def main():
    u_decimal = convert_to_base_10(u)
    t_decimal = convert_to_base_10(t)

    print("U_Decimal: " + str(u_decimal))
    print("T_Decimal: " + str(t_decimal))

    print("This is the sum of the digits of the key: ")
    sum_key_digits = t_decimal // sum_digits(u_decimal)
    print(sum_key_digits)
    # key_binary = t1.convert_to_base_2(key_binary)
    print("-----------------------")

    print("We can now assume we want to transmit a certain message:")
    u_forged = np.array([1, 0, 1, 0, 1])
    print("u_forged = ", u_forged)

    t_forged = tag_computation(
        sum_digits(convert_to_base_10(u_forged)), sum_key_digits
    )
    print("This is the forged tag in base 10: ")
    print(t_forged)
    t_forged = convert_to_base_2(t_forged)
    print("This is the forged tag: ")
    print(t_forged)
    x_forged = np.concatenate((u_forged, t_forged))
    print("This is the forged message: ")
    print(x_forged)

    print("-----------------------")
    print("Verify the Tag.")
    t_prime = verify_tag_task2(x_forged, k)
    print("Is the tag valid? ", np.array_equal(t_forged, t_prime))


if __name__ == "__main__":
    main()