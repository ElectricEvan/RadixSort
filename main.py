import numpy as np
from math import log10
from numpy.random import rand, randint

def main():
    arr = rand_num_gen(1000000)
    print(arr)
    print(radixLSD(arr))


def rand_num_gen(n):
    return randint(1, 1000000, n)


def radixLSD(arr_in):
    # Define Variables
    arr_len = len(arr_in)
    arr_out = [0] * arr_len
    max_num = max(arr_in)

    # Iterate through highest number's digits
    exp = 10
    while max_num / exp >= 0.1:
        prefix_sum = [0] * 10
        arr_out = [0] * arr_len
        # Iterate through the input array and increment the count of the selected digit's number
        for i in range(arr_len):
            prefix_sum[int(arr_in[i] // 10**int(log10(exp)-1) % 10)] += 1
        # Compute the counts into prefix sums
        for i in range(1, 10):
            prefix_sum[i] += prefix_sum[i-1]
        # Compute the new output
        for i in reversed(range(arr_len)):
            # Iterate through the input array and decrement the count of the selected digit's number to get output index
            digit_num = int(arr_in[i] // 10**int(log10(exp)-1) % 10)
            prefix_sum[digit_num] -= 1
            arr_out[prefix_sum[digit_num]] = arr_in[i]
        arr_in = arr_out
        exp *= 10
    return arr_out


if __name__ == "__main__":
    main()
