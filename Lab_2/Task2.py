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


def inverse(m):
    n = []
    for i in range(len(m)):
        if m[i] == 0:
            n.append(1)
        else:
            n.append(0)
    return n


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


import copy

old_ciphe_space = copy.deepcopy(cipher_space)


# uniform binning encoder
def uniform_binning_encoder(m):
    cipher_space = copy.deepcopy(old_ciphe_space)
    flag = False
    # print("Entered uniform_binning_encoder...")
    y = []
    z = []
    n = inverse(m)
    encoding = np.random.randint(0, 2)

    print("The inserted message is", m)
    # verify that the input is in the cipher space
    if not (m in message_space):
        print("The input is not in the message space")
        return None
    else:
        # print("Message " + str(m) + " is in the message space! Continuing...")
        cip_messages = [c[1:4] if c[0] == encoding else None for c in cipher_space]
        if m in cip_messages and encoding == 0:
            #    print("The message is in the chip messages")
            y = cipher_space[cip_messages.index(m)]
        elif n in cip_messages and encoding == 1:
            #    print("The message is in the chip messages")
            y = cipher_space[cip_messages.index(n)]
        else:
            raise Exception("The message is not in the cipher messages")

    return y


def main():
    m = [0, 0, 0]
    print("The input is", m)
    print("The random x is", uniform_binning_encoder(m))


if __name__ == "__main__":
    main()
