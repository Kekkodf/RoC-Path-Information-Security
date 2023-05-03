import numpy as np
import Task1 as t1
import Task2 as t2
import matplotlib.pyplot as plt
from matplotlib import pyplot

epsilon_set = np.arange(0, 1.1, 0.1)
delta_set = np.arange(0, 1.1, 0.1)


def secrecy_capacity(delt, eps):
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
            if np.abs(epsilon - 1 / 2) < np.abs(delta - 1 / 2):
                row.append(secrecy_capacity(epsilon, delta))
            else:
                row.append(0)
        secrecy_capacity_values.append(row)

    secrecy_capacity_values = np.array(secrecy_capacity_values)
    pyplot.figure(figsize=(15, 10))
    # plot |epsilon - 1/2| < |delta - 1/2|
    plt.fill_between(
        epsilon_set,
        delta_set,
        where=(np.abs(epsilon_set - 0.5) < np.abs(delta_set - 0.5)),
        color="black",
    )

    plt.imshow(
        secrecy_capacity_values,
        cmap="viridis",
        interpolation="bilinear",
        extent=[0, 1, 0, 1],
        origin="lower",
    )
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)

    # Plot the diagonal lines
    plt.plot(x, x, "k--", linewidth=2)
    plt.plot(x, 1 - x, "k--", linewidth=2)
    plt.colorbar()
    plt.xlabel("Epsilon")
    plt.ylabel("Delta")
    plt.xlim(0.02, 0.98)
    plt.ylim(0,1)
    plt.show()
    


def plot_secrecy_capacity_3d():
    secrecy_capacity_values = []
    for epsilon in epsilon_set:
        for delta in delta_set:
            secrecy_capacity_values.append(secrecy_capacity(delta, epsilon))
    secrecy_capacity_values = np.array(secrecy_capacity_values).reshape(
        (len(epsilon_set), len(delta_set))
    )
    fig = pyplot.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(epsilon_set, delta_set, secrecy_capacity_values)
    ax.set_xlabel("Epsilon")
    ax.set_ylabel("Delta")
    ax.set_zlabel("Secrecy Capacity")
    ax.set_title("Entropy")
    # pyplot.show()


def main():
    plot_secrecy_capacity()
    plot_secrecy_capacity_3d()


if __name__ == "__main__":
    main()