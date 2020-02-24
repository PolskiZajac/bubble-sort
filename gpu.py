from random import randint
import numpy as np
from numba import cuda, njit, prange
from numba.typed import List
import ctypes


def generator(minV, maxV, amount, numpy=True):
    output = List()
    [output.append(randint(minV, maxV)) for iterate in range(0, amount, 1)]
    if numpy is True:
        np_output = np.array(output)
        return np_output
    else:
        return output


@njit
def bubble_Sort(input_data_list: List):
    number = swaps = i = j = t = 0
    swapped = False

    data = List()
    [data.append(x) for x in input_data_list]
    size = len(data)

    for j in prange(size):
        swapped = False

        for i in prange(size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

    return data
