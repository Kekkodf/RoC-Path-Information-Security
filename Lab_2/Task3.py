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
    for element in cipher_space:
        element = np.array(element)
        hamming_d = t2.hamming_distance(c, element)
        if hamming_d == 1:
            c = element
            break
    c_opposite = []
    m = []
    for i in range(len(c)):
        if c[i] == 0:
            c_opposite.append(1)
        else:
            c_opposite.append(0)
    if c[0] == 0:
        m = c[1:4]
        return m
    if c[0] == 1:
        m = c_opposite[1:4]
        return m

def main():
    c = [1, 0, 1, 1, 0, 1, 0]
    m = uniform_binning_decoder(c)
    print("The input of decoder is:", c)
    print("The output of decoder is:", uniform_binning_decoder(c))
    print("")
    #proove that the decoder is correct
    print("Proof that the decoder is correct. (Encoding + Decoding)")
    print("Encoding the output of the decoder:", t2.uniform_binning_encoder(uniform_binning_decoder(c)))
    print("Decoding the output of the encoder:", uniform_binning_decoder(t2.uniform_binning_encoder(m)))
    print("")
    #proove that the decoder is correct with the legitimate channel
    print("Proof that the decoder is correct with the legitimate channel. (Encoding + Legitimate Channel + Decoding)")
    print("Encoding the output of the decoder:", t2.uniform_binning_encoder(uniform_binning_decoder(c)))
    print("Decoding through the legitimate channel:", uniform_binning_decoder(t1.legitimate_corruption(t2.uniform_binning_encoder(m))))

if __name__ == "__main__":
    main()
    
