import numpy as np
import task1 as t1

x = [1, 0, 1, 0, 0, 1, 1, 1, 0]
u = [1, 0, 1, 0, 0]
t = [1, 1, 1, 0]


def main():
    u_decimal = t1.convert_to_base_10(u)
    t_decimal = t1.convert_to_base_10(t)

    print("U_Decimal: " + str(u_decimal))
    print("T_Decimal: " + str(t_decimal))

    print("This is the sum of the digits of the key: ")
    sum_key_digits = t_decimal // t1.sum_digits(u_decimal)
    print(sum_key_digits)
    # key_binary = t1.convert_to_base_2(key_binary)
    print("-----------------------")

    print("We can now assume we want to transmit a certain message:")
    u_forged = np.array([1, 0, 1, 0, 1])
    print("u_forged = ", u_forged)

    t_forged = t1.tag_computation(
        t1.sum_digits(t1.convert_to_base_10(u_forged)), sum_key_digits
    )
    print("This is the forged tag in base 10: ")
    print(t_forged)
    t_forged = t1.convert_to_base_2(t_forged)
    print("This is the forged tag: ")
    print(t_forged)
    x_forged = np.concatenate((u_forged, t_forged))
    print("This is the forged message: ")
    print(x_forged)

    print("-----------------------")
    print("Verify the Tag.")
    t_prime = t1.verify_tag_task2(x_forged, t1.k)
    print("Is the tag valid? ", np.array_equal(t_forged, t_prime))


if __name__ == "__main__":
    main()
