from random import randint
import numpy as np
from numba import cuda, njit


def generator(minV: int, maxV: int, amount: int) -> np.array:
    output = np.zeros(shape=(amount,), dtype=int)
    for iterate in range(0, amount, 1):
        output[iterate] = (randint(minV, maxV))
    return output


@njit
def bubble_Sort(input_data_list: np.array) -> np.array:
    i = j = 0
    swapped = False
    data = input_data_list.copy()
    size = len(data)
    for j in range(size):
        swapped = False
        for i in range(size - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break
    return data
