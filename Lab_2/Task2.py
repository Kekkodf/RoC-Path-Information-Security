import numpy as np
import matplotlib.pyplot as plt
import random

cipher_space = [[0,0,0,0,0,0,0], [1,0,0,0,1,1,0], [0,1,0,0,1,0,1], [0,0,1,0,0,1,1], [0,0,0,1,1,1,1],
                [1,1,0,0,0,1,1], [1,0,1,0,1,0,1], [1,0,0,1,0,0,1], [0,1,1,0,1,1,0], [0,1,0,1,0,1,0], 
                [0,0,1,1,1,0,0], [1,1,1,0,0,0,0], [1,1,0,1,1,0,0], [1,0,1,1,0,1,0], [0,1,1,1,0,0,1],
                [1,1,1,1,1,1,1]]

#compute the Hamming distance between two vectors
def hamming_distance(v1, v2):
    return np.sum(np.abs(v1 - v2))

#observe that the minimum Hamming distance in the code is 3
#for v1 in cipher_space:
#    for v2 in cipher_space:
#        if not (v1 == v2):
#            print("Hamming distance between", v1, "and", v2, "is", hamming_distance(np.array(v1), np.array(v2)))

message_space = [[0,0,0], [0,0,1], [0,1,0], [1,0,0],
                 [0,1,1], [1,0,1], [1,1,0], [1,1,1]]

#uniform binning encoder
def uniform_binning_encoder(m):
    y = []
    z = []
    #verify that the input is in the cipher space
    if not (m in message_space):
        print("The input is not in the message space")
        return
    else:
        for x in cipher_space:
            if x[0] == 0:
                if x[1:4] == m:
                    y = x
                    break
    #computing the complemnetary code
    for i in range(len(y)):
        if y[i] == 0:
            z.append(1)
        else:
            z.append(0)
    set = [y, z]
    ris = random.choice(set)
    return ris

def main():
  for m in message_space:
    print("The input is", m)
    print("The random x is", uniform_binning_encoder(m))
    if uniform_binning_encoder(m) in cipher_space :
      print('Valid encoding')
    else:
      print('Invalid encoding')
    print(' ')


if __name__ == "__main__":
    main()


