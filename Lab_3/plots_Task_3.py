import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import time
import Task1 as t1
import Task2 as t2

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

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return np.array(sum)

def verify_tag_appropriate_for_this_plot(x, k, u, t_prime):
    u_cap = x[0:len(u)+1]
    t = tag_computation(sum_digits(convert_to_base_10(u_cap)), sum_digits(convert_to_base_10(k)))
    t = convert_to_base_2(t)
    return np.array_equal(t, t_prime)

def main():
    #plot 3d graph x:axis len of u, y:axis len of k, z:time complexity of tag_computation
    x = np.arange(1, 100, 1)
    y = np.arange(1, 100, 1)

    u = []
    k = []

    for i in range(1, 100):
        u.append(np.random.randint(0, 2, i))
        k.append(np.random.randint(0, 2, i))

    z = np.zeros((len(x), len(y)))
    i = 0
    for u_i in u:
        j = 0
        for k_j in k:
            #start
            start = time.time()
            counter = 0
            t = tag_computation(sum_digits(convert_to_base_10(u_i)), sum_digits(convert_to_base_10(k_j)))
            #attack
            u_forged = np.array([1, 0, 1, 0, 1])
            for a in range(280):
                sum_key_digits = a
                t_forged = t1.tag_computation(
                    t1.sum_digits(t1.convert_to_base_10(u_forged)), sum_key_digits
                )
                print("This is the forged tag in base 10: ")
                print(t_forged)
                t_forged = t1.convert_to_base_2(t_forged)
                print("This is the forged tag: ")
                print(t_forged)
                x_forged = np.concatenate((u_forged, t_forged))
                print("This is the forged message: ")
                print(x_forged)
                print("-----------------------")
                print("Verify the Tag.")
                t_prime = t2.verify_tag_task2(x_forged, k_j)
                if np.array_equal(t_forged, t_prime):
                    print("Match Found!")
                    print("The sum_key_digits is: ", sum_key_digits)
                    counter += 1
                    print("The key was found after", counter, "iterations.")
                    break
                else:
                    counter += 1
            end = time.time()
            z[i][j] = end - start
            j += 1
        i += 1
    
    #plot 3d graph
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, z, cmap='viridis')
    ax.set_xlabel('Length of the message')
    ax.set_ylabel('Length of the key')
    ax.set_zlabel('Time complexity under attack in Task 3')
    ax.zaxis.labelpad = 20
    plt.show()


if __name__ == "__main__":
    main()
