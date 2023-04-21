import numpy as np
import Task1 as t1
import Task2 as t2
import Task3 as t3
import Task4 as t4
import Task5 as t5
import matplotlib.pyplot as plt
from matplotlib import pyplot
import random

#see settings in Task5.py
epsilon = t5.epsilon
delta = t5.delta

messages = t2.message_space

ciphers_clear = t2.cipher_space

if (abs((epsilon - 0.5))<abs(delta - 0.5)):
    corrupted_ciphers = []
    for i,m in zip(range(len(ciphers_clear)),messages):
        corrupted_ciphers.append(t1.legitimate_corruption(t2.uniform_binning_encoder(m)))
        print("Added corrupted cipher:", corrupted_ciphers[i])

if (abs((epsilon - 0.5))>abs(delta - 0.5)):
    corrupted_ciphers = []
    for i,m in zip(range(len(ciphers_clear)),messages):
        corrupted_ciphers.append(t1.eavesdropper_corruption(t2.uniform_binning_encoder(m)))
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
