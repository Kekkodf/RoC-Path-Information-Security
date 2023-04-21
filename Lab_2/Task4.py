import numpy as np
import task1 as t1
import task2 as t2
import task3 as t3
import matplotlib.pyplot as plt
from matplotlib import pyplot
import random

messages = t2.message_space

ciphers_clear = t2.cipher_space

corrupted_ciphers = []
for i in range(len(ciphers_clear)):
    corrupted_ciphers.append(t1.eavesdropper_corruption(ciphers_clear[i]))
    print("Added corrupted cipher:", corrupted_ciphers[i])


def run_10k_times(corrupted_ciphers):
    # run the decoder 10k times
    eavesdropper_channel_error_counters = {}
    for error in corrupted_ciphers:
        eavesdropper_channel_error_counters[tuple(error)] = 0
    for i in range(20000):
        # message = t1.xor(message, corrupted_ciphers[i])
        eavesdropper_channel_random_error = random.choice(corrupted_ciphers)
        eavesdropper_channel_error_counters[
            tuple(eavesdropper_channel_random_error)
        ] += 1

    return eavesdropper_channel_error_counters


def compute_empirical_distribution(eavesdropper_channel_error_counters):
    # compute the empirical distribution of the eavesdropper channel
    empirical_distribution = {}
    for error in eavesdropper_channel_error_counters:
        empirical_distribution[error] = (
            eavesdropper_channel_error_counters[error] / 10000
        )
    return empirical_distribution


# plot the results
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
    plot_corrupted_ciphers(run_10k_times(corrupted_ciphers))


if __name__ == "__main__":
    main()
