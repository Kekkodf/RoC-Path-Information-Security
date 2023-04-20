import numpy as np
import matplotlib.pyplot as plt
import random
import Task1 as t1
import Task2 as t2

cipher_space = [[0,0,0,0,0,0,0], [1,0,0,0,1,1,0], [0,1,0,0,1,0,1], [0,0,1,0,0,1,1], [0,0,0,1,1,1,1],
                [1,1,0,0,0,1,1], [1,0,1,0,1,0,1], [1,0,0,1,0,0,1], [0,1,1,0,1,1,0], [0,1,0,1,0,1,0], 
                [0,0,1,1,1,0,0], [1,1,1,0,0,0,0], [1,1,0,1,1,0,0], [1,0,1,1,0,1,0], [0,1,1,1,0,0,1],
                [1,1,1,1,1,1,1]]

def uniform_binning_decoder(c):
    #compute the opposite of the input
    c_opposite = []
    m = []
    for i in range(len(c)):
        if c[i] == 0:
            c_opposite.append(1)
        else:
            c_opposite.append(0)
    if (c in cipher_space or c_opposite in cipher_space):
        if c[0] == 0:
            m = c[1:4]
            return m
        if c[0] == 1:
            m = c_opposite[1:4]
            return m
    else:
        print("The input is not in the cipher space")
        return

def main():
    c = [0, 1, 0, 0, 1, 0, 1]
    m = uniform_binning_decoder(c)
    print("The input of decoder is:", c)
    print("The output of decor is:", uniform_binning_decoder(c))
    print("")
    #proove that the decoder is correct
    print("Proof that the decoder is correct. (Encoding + Decoding)")
    print("Encoding the output of the decoder:", t2.uniform_binning_encoder(uniform_binning_decoder(c)))
    print("Decoding the output of the encoder:", uniform_binning_decoder(t2.uniform_binning_encoder(m)))
    print("")
    #proove that the decoder is correct with the legitimate channel
    print("Proof that the decoder is correct with the legitimate channel. (Encoding+Legitimate Channel+Decoding)")


if __name__ == "__main__":
    main()
    
