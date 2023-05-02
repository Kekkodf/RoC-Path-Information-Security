import random
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
from statistics import mean, stdev

input_given = [0, 0, 0, 0, 0, 0, 0]


def xor(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] ^ b[i]
    return c


def legitimate_corruption(input_given):
    legitimate_channel_random_error = random.choice(legitimate_channel_error)
    return xor(input_given, legitimate_channel_random_error)


def eavesdropper_corruption(input_given):
    eavesdropper_channel_random_error = random.choice(eavesdropper_channel_error)
    return xor(input_given, eavesdropper_channel_random_error)


# all possible corruption of the message
# we considered all possible combination of bits
# where the Hamming distance is =< 3 with the original message
legitimate_channel_error = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
]

eavesdropper_channel_error = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
]


def hamming_distance(str1, str2):
    # Calculate the Hamming distance
    hamming_dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamming_dist += 1
    return hamming_dist


# compute where the eavesdropper channel error is hamming distance <=3 from the input
list1 = []
for vector in eavesdropper_channel_error:
    if hamming_distance(input_given, vector) <= 3:
        list1.append(vector)

list2 = []
for vector in legitimate_channel_error:
    if hamming_distance(input_given, vector) <= 1:
        list2.append(vector)


def limited_corruption(value):
    list1 = []
    for vector in eavesdropper_channel_error:
        if hamming_distance(value, vector) <= 3:
            list1.append(vector)

    eavesdropper_channel_random_error = random.choice(list1)
    return xor(value, eavesdropper_channel_random_error)


def main():
    input_given = [0, 0, 0, 0, 0, 0, 0]
    # define two dictionaries to count the number of occurences of each error. The keys are the errors and the values are the number of occurences
    legitimate_channel_error_counters = {}
    eavesdropper_channel_error_counters = {}

    # initialize the counters to 0
    for error in list1:
        eavesdropper_channel_error_counters[tuple(error)] = 0

    for error in list2:
        legitimate_channel_error_counters[tuple(error)] = 0

    for i in range(10000):
        # choose a random error from the list of errors
        legitimate_channel_random_error = random.choice(list2)
        eavesdropper_channel_random_error = random.choice(list1)

        print("input_given_given: ", input_given)
        print("-----------------------------")

        # apply the legitimate channel error
        print(
            "MESSAGE RECEIVED ON THE LEGITIMATE CHANNEL: "
            + str(xor(input_given, legitimate_channel_random_error))
        )
        print(
            "MESSAGE RECEIVED ON THE EAVESDROPPER CHANNEL: "
            + str(xor(input_given, eavesdropper_channel_random_error))
        )

        print("-----------------------------")

        # count the number of occurences of each error with the dictionaries
        legitimate_channel_error_counters[tuple(legitimate_channel_random_error)] += 1

        eavesdropper_channel_error_counters[
            tuple(eavesdropper_channel_random_error)
        ] += 1

        # print("LEGITIMATE CHANNEL ERROR COUNTERS: ", legitimate_channel_error_counters)
        # print(
        #    "EAVESDROPPER CHANNEL ERROR COUNTERS: ", eavesdropper_channel_error_counters
        # )

        print("NEXT ITERATION")

    print("-----------------------------")
    print("EXITING THE LOOP")
    print("-----------------------------")

    print("LEGITIMATE CHANNEL ERROR COUNTERS: ", legitimate_channel_error_counters)
    print("EAVESDROPPER CHANNEL ERROR COUNTERS: ", eavesdropper_channel_error_counters)

    print("-----------------------------")
    print(
        "MEAN ERROR RATE OF THE LEGITIMATE CHANNEL: ",
        mean(legitimate_channel_error_counters.values()),
    )
    print("-----------------------------")
    print(
        "MEAN ERROR RATE OF THE EAVESDROPPER CHANNEL: ",
        mean(eavesdropper_channel_error_counters.values()),
    )
    print("-----------------------------")
    print("-----------------------------")
    print(
        "STANDARD DEVIATION OF THE LEGITIMATE CHANNEL: ",
        stdev(legitimate_channel_error_counters.values()),
    )
    print("-----------------------------")
    print(
        "STANDARD DEVIATION OF THE EAVESDROPPER CHANNEL: ",
        stdev(eavesdropper_channel_error_counters.values()),
    )

    for error in eavesdropper_channel_error_counters:
        if error not in legitimate_channel_error_counters:
            legitimate_channel_error_counters[error] = 0

    # plot the results
    # figure size
    pyplot.figure(figsize=(20, 30))

    plt.bar(
        range(len(legitimate_channel_error_counters)),
        legitimate_channel_error_counters.values(),
        align="edge",
    )

    plt.bar(
        range(len(eavesdropper_channel_error_counters)),
        eavesdropper_channel_error_counters.values(),
        align="center",
    )

    plt.xticks(
        range(len(legitimate_channel_error_counters)),
        list(legitimate_channel_error_counters.keys()),
    )
    plt.legend(["Legitimate Channel", "Eavesdropper Channel"])
    # reduce the size of the xticks
    plt.xticks(rotation=90)
    plt.xticks(fontsize=3)

    plt.show()


if __name__ == "__main__":
    main()
