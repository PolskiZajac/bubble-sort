from random import randint
import numpy as np
from numba import cuda, jit, njit
from numba.typed import List


def generator(minV, maxV, amount, numpy=True):
    output = []
    for iterate in range(0, amount, 1):
        output.append(randint(minV, maxV))
    if numpy is True:
        np_output = np.array(output)
        return np_output
    else:
        return output


@jit
def bubble_Sort(input_data_list: list):
    number = swaps = i = j = t = int(0)
    swapped = False

    data = List()
    data = input_data_list.copy()
    size = len(data)

    for j in range(size):
        swapped = False

        for i in range(0, size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

    return data


assert not bubble_Sort.nopython_signatures
