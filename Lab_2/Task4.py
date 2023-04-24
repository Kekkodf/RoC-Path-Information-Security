import numpy as np
import task1 as t1
import task2 as t2
import matplotlib.pyplot as plt
from matplotlib import pyplot

messages_list = message_space = [
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


def run_10k_times(message):
    eavesdropper_channel_error_counters = {}
    for error in potential_corrupted_ciphers:
        error = np.asarray(error)
        eavesdropper_channel_error_counters[tuple(error)] = 0

    for i in range(5000):
        print("Message: ", message)
        transmitted = t2.uniform_binning_encoder(message)
        if transmitted is None:
            continue
        print("Transmitted message: ", transmitted)
        corrupted = t1.eavesdropper_corruption(transmitted)
        print("Corrupted message: ", corrupted)
        eavesdropper_channel_error_counters[tuple(corrupted)] += 1
        print("Added 1 to ", corrupted)

    return eavesdropper_channel_error_counters


def compute_empirical_distribution(eavesdropper_channel_error_counters):
    # compute the empirical distribution of the eavesdropper channel
    empirical_distribution = {}
    for error in eavesdropper_channel_error_counters:
        empirical_distribution[error] = (
            eavesdropper_channel_error_counters[error] / 10000
        )
    return empirical_distribution


def plot_corrupted_ciphers(eavesdropper_channel_error_counters):
    pyplot.figure(figsize=(10, 15))

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

    plt.show()

    pyplot.figure(figsize=(10, 15))

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
    message = [1, 1, 1]
    print("Message:", message)
    print("Starting the 10k iterations w/corruption...")
    print("-------------------------------------------")
    plot_corrupted_ciphers(run_10k_times(message))
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
