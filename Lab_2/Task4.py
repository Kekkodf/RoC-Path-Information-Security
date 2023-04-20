import numpy as np
import Task1 as t1
import Task2 as t2
import Task3 as t3
import matplotlib.pyplot as plt
import random

messagges = t2.message_space

ciphers_clear = t2.cipher_space

corrupted_ciphers = []
for i in range(len(ciphers_clear)):
    corrupted_ciphers.append(t1.eavesdropper_corruption(ciphers_clear[i]))

def run_10k_times(corrupted_ciphers):
    #run the decoder 10k times
    eavesdropper_channel_error_counters = {}
    for error in corrupted_ciphers:
        eavesdropper_channel_error_counters[tuple(error)] = 0
    for i in range(10000):
        eavesdropper_channel_random_error = random.choice(corrupted_ciphers)
        eavesdropper_channel_error_counters[tuple(eavesdropper_channel_random_error)] += 1

    return eavesdropper_channel_error_counters

#plot the results
def plot_corrupted_ciphers(eavesdropper_channel_error_counters):
    plt.bar(eavesdropper_channel_error_counters.keys(), eavesdropper_channel_error_counters.values(), color='g')
    plt.show()    

def main():
    plot_corrupted_ciphers(run_10k_times(corrupted_ciphers))

if __name__ == "__main__":
    main()