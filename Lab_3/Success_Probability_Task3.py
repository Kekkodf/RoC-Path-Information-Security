import matplotlib.pyplot as plt

def max_sum_digits(x):
    max_val = 2**x - 1
    max_sum = 0
    for i in range(max_val + 1):
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum > max_sum:
            max_sum = digit_sum
    return max_sum

x = range(1, 25)
y = [1/max_sum_digits(i) for i in x]

plt.plot(x, y)
plt.xlabel('Length of the key')
plt.ylabel('Probability of success')
plt.show()
