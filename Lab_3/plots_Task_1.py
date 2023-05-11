import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import time

def convert_to_base_10(u):
    u_base_10 = 0
    for i in range(len(u)):
        u_base_10 += u[i]*2**(len(u)-1-i)
    return u_base_10

def convert_to_base_2(t):
    t_base_2 = []
    while t:
        t_base_2.append(t % 2)
        t //= 2
    return np.array(t_base_2)

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def tag_computation(u,k):
    return convert_to_base_2(u*k)

def verify_tag_appropriate_for_this_plot(x, k, u, t_prime):
    u_cap = x[0:len(u)+1]
    t = tag_computation(sum_digits(convert_to_base_10(u_cap)), sum_digits(convert_to_base_10(k)))
    t = convert_to_base_2(t)
    return np.array_equal(t, t_prime)

def main():
    #plot 3d graph x:axis len of u, y:axis len of k, z:time complexity of tag_computation
    x = np.arange(1, 100, 1)
    y = np.arange(1, 100, 1)

    z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            u = np.random.randint(0,2,x[i])
            k = np.random.randint(0,2,y[j])
            start = time.time()
            t = tag_computation(sum_digits(convert_to_base_10(u)), sum_digits(convert_to_base_10(k)))
            #concatenate u and t
            u_1 = np.concatenate((u,t))
            #verify tag
            u_2 = u_1[0:len(u)+1]
            t = tag_computation(sum_digits(convert_to_base_10(u_2)), sum_digits(convert_to_base_10(k)))
            end = time.time()
            z[i][j] = end - start
    
    #plot 3d graph
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, z, cmap='viridis')
    ax.set_xlabel('Length of the message')
    ax.set_ylabel('Length of the key')
    #ax.set_zlabel('Time complexity of tag computation')
    ax.set_zlabel('Time complexity of tag verification')
    ax.zaxis.labelpad = 20
    plt.show()


if __name__ == "__main__":
    main()
