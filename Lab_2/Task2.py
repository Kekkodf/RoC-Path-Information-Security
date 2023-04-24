import numpy as np
import matplotlib.pyplot as plt
import random

cipher_space = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]


# compute the Hamming distance between two vectors
def hamming_distance(v1, v2):
    return np.sum(np.abs(v1 - v2))


# observe that the minimum Hamming distance in the code is 3
# for v1 in cipher_space:
#    for v2 in cipher_space:
#        if not (v1 == v2):
#            print("Hamming distance between", v1, "and", v2, "is", hamming_distance(np.array(v1), np.array(v2)))

message_space = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]


def pmd(x, y):
    # verify that the inputs are in the cipher space
    if not (x in cipher_space and y in cipher_space):
        print("The inputs are not in the cipher space")
        return
    else:
        # compute the Hamming distance between x and y
        return hamming_distance(np.array(x), np.array(y)) / 7


# uniform binning encoder
def uniform_binning_encoder(m):
    print("Entered uniform_binning_encoder...")
    y = []
    z = []
    print("The inserted message is", m)
    # verify that the input is in the cipher space
    if not (m in message_space):
        print("The input is not in the message space")
        return None
    else:
        print("Message is in message space! Continuing...")
        for x in cipher_space:
            if x[0] == 0:
                if x[1:4] == m:
                    print("Found the match! X is", x)
                    y = x
                    print("Exiting")
                    break
                else:
                    print(
                        "Checked for "
                        + str(x)
                        + " and "
                        + str(m)
                        + " is yet to be found"
                    )
    # computing the complementary code
    for i in range(len(y)):
        if y[i] == 0:
            z.append(1)
            print("Appended 1 to z")
        else:
            z.append(0)
            print("Appended 0 to z")
    set = [y, z]
    print(set)
    ris = random.choice(set)
    return ris


def main():
    m = [1, 0, 0]
    print("The input is", m)
    print("The random x is", uniform_binning_encoder(m))


if __name__ == "__main__":
    main()
