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

def areEqual(arr1, arr2, N, M):
 
    # If lengths of array are not
    # equal means array are not equal
    if (N != M):
        return False
 
    # Sort both arrays
    arr1.sort()
    arr2.sort()
 
    # Linearly compare elements
    for i in range(0, N):
        if (arr1[i] != arr2[i]):
            return False
 
    # If all elements were same.
    return True

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
            if areEqual(x[1:4], m, len(x[1:4]), len(m)):
                y = x
                break
    #computing the complemnetary code
    for i in range(len(y)):
        if y[i] == 0:
            z.append(1)
        else:
            z.append(0)
    return y, z

def main():
    m = [1,0,0]
    print("The input is", m)
    print("The output is", uniform_binning_encoder(m))

if __name__ == "__main__":
    main()


