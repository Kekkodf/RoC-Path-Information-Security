import numpy as np
import Task1 as t1
import Task2 as t2
import Task3 as t3
import matplotlib.pyplot as plt
import random

#eavsdropper channel corruption example
epsilon = 0.1
delta = 0.2

#legitimate channel corruption example
#epsilon = 0.2
#delta = 0.1

def BSC(epsilon, delta, m):
    if (abs((epsilon - 0.5))<abs(delta - 0.5)):
        v = t1.legitimate_corruption(t2.uniform_binning_encoder(m))
        ans = []
        for i in range(len(v)):
            ans.append(v[i])
        return ans
    if (abs(epsilon - 0.5)>abs(delta - 0.5)):
        v = t1.eavesdropper_corruption(t2.uniform_binning_encoder(m))
        ans = []
        for i in range(len(v)):
            ans.append(v[i])
        return ans

def main():
    print("If 0 < delta < epsilon < 0.5") #legitimate channel is degraded
    print("If 0 < epsilon < delta < 0.5") #eavesdropper channel is degraded
    print("Epsilon is set to:", epsilon)
    print("Delta is set to:", delta)
    print("")
    #create a random message
    count_correctly_matched = 0
    count_missmatched = 0
    for i in range(7):
        m = []
        for i in range(3):
            m.append(random.randint(0, 1))
        print("The input is:", m)
        bsc_enc = BSC(epsilon, delta, m)
        print("The random x, after BSC, is:", bsc_enc)
        bsc_dec = t3.uniform_binning_decoder(bsc_enc)
        print("The output of the decoding is:", bsc_dec)
        print("")
        print("See if secrecy is reached or not.")
        print("The input is:", m)
        print("The output of the decoding is:", bsc_dec)
        m_vec = np.array(m)
        bsc_dec_vec = np.array(bsc_dec)
        print("The Hamming distance is:", t2.hamming_distance(m_vec, bsc_dec_vec))
        print(" ")
        if t2.hamming_distance(m_vec, bsc_dec_vec) == 0:
            count_correctly_matched += 1
        else:
            count_missmatched += 1
    print("The number of correctly matched messages is:", count_correctly_matched)
    print("The number of missmatched messages is:", count_missmatched)


if __name__ == "__main__":
    main()