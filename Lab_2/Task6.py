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

epsilon_range = np.arange(0, 0.5, 0.01)
delta_range = np.arange(0, 0.5, 0.01)

def secrecy_capacity(epsilon, delta):
    return h2(delta) - h2(epsilon)

def h2(x):
    return -x*np.log2(x) - (1-x)*np.log2(1-x)

def plot_secrecy_capacity():
    secrecy_capacity_values = []
    for epsilon in epsilon_range:
        for delta in delta_range:
            secrecy_capacity_values.append(secrecy_capacity(epsilon, delta))
    secrecy_capacity_values = np.array(secrecy_capacity_values).reshape((len(epsilon_range), len(delta_range)))
    plt.imshow(secrecy_capacity_values, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()

def plot_secrecy_capacity_3d():
    secrecy_capacity_values = []
    for epsilon in epsilon_range:
        for delta in delta_range:
            secrecy_capacity_values.append(secrecy_capacity(epsilon, delta))
    secrecy_capacity_values = np.array(secrecy_capacity_values).reshape((len(epsilon_range), len(delta_range)))
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(epsilon_range, delta_range, secrecy_capacity_values)
    pyplot.show()

def main():
    plot_secrecy_capacity()
    plot_secrecy_capacity_3d()

if __name__ == "__main__":
    main()
