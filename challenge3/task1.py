import numpy as np

k = np.array([1, 1, 1])
u = np.array([1,0,1])

def convert_to_base_10(u):
    u_base_10 = 0
    for i in range(len(u)):
        u_base_10 += u[i]*2**(len(u)-1-i)
    return np.array(u_base_10)

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
    return np.array(sum)

def tag_computation(u,k):
    return np.array(u*k)

def verify_tag(x, k):
    u_1 = x[0:len(u)]
    print("u = ", u_1)
    print("k = ", k)
    t = tag_computation(sum_digits(convert_to_base_10(u_1)), sum_digits(convert_to_base_10(k)))
    t = convert_to_base_2(t)
    return t

def main():
    print("-----------------------")
    print("u = ", u)
    print("k = ", k)
    t = tag_computation(sum_digits(convert_to_base_10(u)), sum_digits(convert_to_base_10(k)))
    t = convert_to_base_2(t)
    print("t = ", t)
    x = np.concatenate((u,t))
    print("x = ", x)
    print("-----------------------")
    print("Verify the Tag.")
    t_prime = verify_tag(x, k)
    print("Is the tag correct? ", np.array_equal(t, t_prime))
    print("-----------------------")

if __name__ == "__main__":
    main()
