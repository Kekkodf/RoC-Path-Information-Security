import random
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
from statistics import mean, stdev


def xor(a, b):
    for i in range(len(a)):
        a[i] = a[i] ^ b[i]
    return a


def legitimate_corruption(input):
    legitimate_channel_random_error = random.choice(legitimate_channel_error)
    xor(input, legitimate_channel_random_error)
    return input


def eavesdropper_corruption(input):
    eavesdropper_channel_random_error = random.choice(eavesdropper_channel_error)
    xor(input, eavesdropper_channel_random_error)
    return input


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
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
]


def main():
    input = [1, 0, 1, 0, 1, 0, 0]

    # define two dictionaries to count the number of occurences of each error. The keys are the errors and the values are the number of occurences
    legitimate_channel_error_counters = {}
    eavesdropper_channel_error_counters = {}

    # initialize the counters to 0
    for error in legitimate_channel_error:
        legitimate_channel_error_counters[tuple(error)] = 0

    for error in eavesdropper_channel_error:
        eavesdropper_channel_error_counters[tuple(error)] = 0

    for i in range(10000):
        input = [1, 0, 1, 0, 1, 0, 0]

        legitimate_channel_random_error = random.choice(legitimate_channel_error)
        eavesdropper_channel_random_error = random.choice(eavesdropper_channel_error)

        print("INPUT: ", input)
        print("-----------------------------")

        # apply the legitimate channel error
        print(
            "MESSAGE RECEIVED ON THE LEGITIMATE CHANNEL: "
            + str(xor(input, legitimate_channel_random_error))
        )
        print(
            "MESSAGE RECEIVED ON THE EAVESDROPPER CHANNEL: "
            + str(xor(input, eavesdropper_channel_random_error))
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
    pyplot.figure(figsize=(10, 15))

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
    plt.xticks(fontsize=6)

    plt.show()


if __name__ == "__main__":
    main()
