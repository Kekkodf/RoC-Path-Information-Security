import numpy as np
import Task1 as t1
import Task2 as t2
import matplotlib.pyplot as plt
from matplotlib import pyplot

epsilon_set = np.arange(0, 1.1, 0.1)
delta_set = np.arange(0, 1.1, 0.1)


def secrecy_capacity(eps, delt):
    return h2(delt) - h2(eps)


def h2(p):
    # log base 1/2 of p
    return -np.log2(p) * p - np.log2(1 - p) * (1 - p)


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

def plot_secrecy_capacity():
    epsilon_set = np.linspace(0, 1, num=100)
    delta_set = np.linspace(0, 1, num=100)

    secrecy_capacity_values = []
    for epsilon in epsilon_set:
        row = []
        for delta in delta_set:
            row.append(secrecy_capacity(epsilon, delta))
        secrecy_capacity_values.append(row)

    secrecy_capacity_values = np.array(secrecy_capacity_values)
    pyplot.figure(figsize=(15,10))
    plt.imshow(
        secrecy_capacity_values,
        cmap="hot",
        interpolation="bilinear",
        extent=[0, 1, 0, 1],
        origin="lower",
    )
    plt.colorbar()
    plt.xlabel("Epsilon")
    plt.ylabel("Delta")
    plt.show()


def plot_secrecy_capacity_3d():
    secrecy_capacity_values = []
    for epsilon in epsilon_set:
        for delta in delta_set:
            secrecy_capacity_values.append(secrecy_capacity(epsilon, delta))
    secrecy_capacity_values = np.array(secrecy_capacity_values).reshape(
        (len(epsilon_set), len(delta_set))
    )
    fig = pyplot.figure(figsize=(15,10))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(epsilon_set, delta_set, secrecy_capacity_values)
    ax.set_xlabel("Epsilon")
    ax.set_ylabel("Delta")
    ax.set_zlabel("Secrecy Capacity")
    ax.set_title("Entropy")
    pyplot.show()


def main():
    plot_secrecy_capacity()
    plot_secrecy_capacity_3d()


if __name__ == "__main__":
    main()