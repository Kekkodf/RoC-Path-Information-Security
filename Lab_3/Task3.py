import Task1 as t1
import Task2 as t2
import numpy as np


def main():
    # in this code we'll assume a specific key size, hence a specific max sum_key_digits value.
    counter = 0
    print("We can now assume we want to transmit a FIXED message:")

    u_forged = np.array([1, 0, 1, 0, 1])

    print("u_forged = ", u_forged)

    for i in range(57):
        sum_key_digits = i
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
        if np.array_equal(t_forged, t_prime):
            print("Match Found!")
            print("The sum_key_digits is: ", sum_key_digits)
            counter += 1
            print("The key was found after", counter, "iterations.")
            break
        else:
            counter += 1


if __name__ == "__main__":
    main()
