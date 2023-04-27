import numpy as np
import Task1 as t1
import Task2 as t2
import Task3 as t3
import matplotlib.pyplot as plt
import random
from matplotlib import pyplot

#eavsdropper channel corruption example (0 < epsilon < delta < 1/2)
epsilon = 0.1
delta = 0.2

#legitimate channel corruption example (0 < delta < epsilon < 1/2)
#epsilon = 0.2
#delta = 0.1

#define the number of trials
number_trials = 100000

def BSC(epsilon, delta, m):
    if (abs((epsilon - 0.5))<abs(delta - 0.5)):
        v = t1.legitimate_corruption(t2.uniform_binning_encoder(m))
        return v
    if (abs(epsilon - 0.5)>abs(delta - 0.5)):
        v = t1.eavesdropper_corruption(t2.uniform_binning_encoder(m))
        return v
    else:
        return None

def main():
    print("If 0 < delta < epsilon < 0.5") #legitimate channel is degraded
    print("If 0 < epsilon < delta < 0.5") #eavesdropper channel is degraded
    print("Epsilon is set to:", epsilon)
    print("Delta is set to:", delta)
    print("")
    #create a random message
    count_correctly_matched = 0
    count_missmatched = 0
    for i in range(number_trials):
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

    #plot the results in a barh graph
    objects = ('Correctly decoded', 'Missmatched')
    y_pos = np.arange(len(objects))
    performance = [count_correctly_matched/number_trials, count_missmatched/number_trials]
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Percentage of messages')
    plt.show()
    
    #save as png
    plt.savefig('Task5_leg_channel_corruption.png')

if __name__ == "__main__":
    main()