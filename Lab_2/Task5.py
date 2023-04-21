import numpy as np
import Task1 as t1
import Task2 as t2
import Task3 as t3
import matplotlib.pyplot as plt
import random

messages = t2.message_space

ciphers_clear = t2.cipher_space

def BSC(epsilon, delta, m):
    if (np.abs(epsilon - 0.5)<np.abs(delta - 0.5)):
        return t1.legitimate_corruption(t2.uniform_binning_encoder(m))
    if (np.abs(epsilon - 0.5)>np.abs(delta - 0.5)):
        return t1.eavesdropper_corruption(t2.uniform_binning_encoder(m))
    else:
        raise ValueError

def main():
    print("If 0 < delta < epsilon < 0.5")
    print("If 0 < epsilon < delta < 0.5")
    epsilon = float(input("Enter epsilon: "))
    delta = float(input("Enter delta: "))
    print("")
    #create a random message
    m = []
    for i in range(20):
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
    print("The Hamming distance is:", t2.hamming_distance(m, bsc_dec))
    print(" ")
if __name__ == "__main__":
    main()