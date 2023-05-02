import numpy as np
import Task1 as t1
import Task2 as t2
import matplotlib.pyplot as plt
from matplotlib import pyplot

message_space = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]

potential_corrupted_ciphers = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
]


def run_15k_times(message):
    eavesdropper_channel_error_counters = {}

    for i in range(15000):
        transmitted = t2.uniform_binning_encoder(message)
        print("Transmitted message: ", transmitted)
        corrupted = t1.limited_corruption(transmitted)
        print("Corrupted message: ", corrupted)
        if tuple(corrupted) not in eavesdropper_channel_error_counters.keys():
            eavesdropper_channel_error_counters[tuple(corrupted)] = 0
        else:
            eavesdropper_channel_error_counters[tuple(corrupted)] += 1
        # print("Corrupted message: ", corrupted)
        # eavesdropper_channel_error_counters[tuple(corrupted)] += 1
        # print("Added 1 to ", corrupted)

    return eavesdropper_channel_error_counters


def compute_empirical_distribution(eavesdropper_channel_error_counters):
    # compute the empirical distribution of the eavesdropper channel
    empirical_distribution = {}
    for error in eavesdropper_channel_error_counters:
        empirical_distribution[error] = (
            eavesdropper_channel_error_counters[error] / 15000
        )
    return empirical_distribution


def plot_corrupted_ciphers(eavesdropper_channel_error_counters):
    pyplot.figure(figsize=(25, 15))

    plt.bar(
        range(len(eavesdropper_channel_error_counters)),
        eavesdropper_channel_error_counters.values(),
        align="edge",
    )

    plt.xticks(
        range(len(eavesdropper_channel_error_counters)),
        list(eavesdropper_channel_error_counters.keys()),
    )
    plt.xticks(rotation=90)
    plt.xticks(fontsize=6)

    # add uniformity threshold

    plt.show()

    pyplot.figure(figsize=(25, 15))

    # save the empirical distribution as .png

    # plot the empirical distribution
    empirical_distribution = compute_empirical_distribution(
        eavesdropper_channel_error_counters
    )
    plt.bar(
        range(len(empirical_distribution)),
        empirical_distribution.values(),
        align="edge",
    )

    plt.xticks(
        range(len(empirical_distribution)),
        list(empirical_distribution.keys()),
    )
    plt.xticks(rotation=90)
    plt.xticks(fontsize=6)

    plt.show()


def main():
    # for message in messages_list:
    np.random.seed(0)
    message = [1, 0, 0]
    # for message in message_space:
    print("Message:", message)
    print("Starting the 15k iterations w/corruption...")
    print("-------------------------------------------")
    plot_corrupted_ciphers(run_15k_times(message))
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
